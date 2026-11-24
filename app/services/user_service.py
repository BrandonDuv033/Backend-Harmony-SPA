from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.domain.enums.user_role import UserRole
from app.models.user import User
from app.models.client_profile import ClientProfile
from app.models.employee_profile import EmployeeProfile
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate
from datetime import datetime, timezone
from sqlalchemy import update
from app.models.user_session import UserSession


class UserServiceError(Exception):
    pass


class UserNotFoundError(UserServiceError):
    pass


class UserAlreadyExistsError(UserServiceError):
    pass


class UserService:

    @staticmethod
    def create_user(db: Session, data: UserCreate) -> User:

        email = str(data.email).strip().lower()

        if UserRepository.get_by_email(db, email):
            raise UserAlreadyExistsError(
                "Ya existe un usuario registrado con ese correo."
            )

        user = User(
            first_name=data.first_name.strip(),
            last_name=data.last_name.strip(),
            email=email,
            phone=data.phone,
            password_hash=hash_password(data.password),
            role=data.role,
            is_active=True,
        )

        try:
            db.add(user)
            db.flush()

            if data.role == UserRole.CLIENTE:
                profile_data = data.client_profile.model_dump()
                db.add(ClientProfile(user_id=user.id, **profile_data))

            elif data.role in (UserRole.ADMIN, UserRole.ESTETICISTA):
                profile_data = data.employee_profile.model_dump()
                db.add(EmployeeProfile(user_id=user.id, **profile_data))

            db.commit()
            db.refresh(user)

            return user

        except IntegrityError as exc:
            db.rollback()
            raise UserAlreadyExistsError(
                "No fue posible registrar el usuario. "
                "Verifica que el correo no esté duplicado."
            ) from exc

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def get_user(db: Session, user_id: int) -> User:

        user = UserRepository.get_by_id(db, user_id)

        if user is None:
            raise UserNotFoundError("No se encontró el usuario solicitado.")

        return user

    @staticmethod
    def list_users(
        db: Session,
        role: UserRole | None = None,
        is_active: bool | None = None,
        skip: int = 0,
        limit: int = 50,
    ) -> list[User]:

        return UserRepository.list_users(
            db=db,
            role=role,
            is_active=is_active,
            skip=skip,
            limit=limit,
        )

    @staticmethod
    def update_user(
        db: Session,
        user_id: int,
        data: UserUpdate,
    ) -> User:

        user = UserService.get_user(db, user_id)

        if user.role == UserRole.SUPER_ADMIN:
            raise UserServiceError(
                "No se puede modificar el SUPER_ADMIN desde este módulo."
            )

        changes = data.model_dump(exclude_unset=True)

        if "email" in changes and changes["email"] is not None:
            changes["email"] = str(changes["email"]).strip().lower()

            existing = UserRepository.get_by_email(db, changes["email"])

            if existing is not None and existing.id != user.id:
                raise UserAlreadyExistsError(
                    "Ese correo electrónico ya está registrado."
                )

        for field, value in changes.items():
            if isinstance(value, str):
                value = value.strip()

            setattr(user, field, value)

        try:
            db.commit()
            db.refresh(user)
            return user

        except IntegrityError as exc:
            db.rollback()
            raise UserAlreadyExistsError(
                "No fue posible actualizar el usuario. "
                "Verifica que el correo no esté duplicado."
            ) from exc

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def change_status(
        db: Session,
        user_id: int,
        is_active: bool,
        current_user_id: int,
    ) -> User:

        user = UserService.get_user(db, user_id)

        if user.role == UserRole.SUPER_ADMIN:
            raise UserServiceError("No se puede cambiar el estado del SUPER_ADMIN.")

        if user.id == current_user_id and not is_active:
            raise UserServiceError("No puedes desactivar tu propia cuenta.")

        user.is_active = is_active

        if not is_active:
            now = datetime.now(timezone.utc).replace(tzinfo=None)

            db.execute(
                update(UserSession)
                .where(
                    UserSession.user_id == user.id,
                    UserSession.is_active.is_(True),
                )
                .values(
                    is_active=False,
                    revoked_at=now,
                )
            )

        db.commit()

        try:
            db.commit()
            db.refresh(user)
            return user

        except Exception:
            db.rollback()
            raise
