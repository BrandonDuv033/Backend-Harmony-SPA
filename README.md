# Backend-Harmony-SPA

API backend construida con **FastAPI** para la gestión del sistema Harmony Spa, aplicando una **arquitectura por capas** (Domain, Infrastructure, API, Models, Schemas, Services, Repositories).

**Estado:** En exploración y desarrollo activo (Fase 2: Configuración de persistencia, ORM y migraciones).

---

## Tabla de contenido

1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Configuración](#configuración)
4. [Migraciones de Base de Datos](#migraciones-de-base-de-datos)
5. [Ejecución](#ejecución)
6. [Pruebas](#pruebas)
7. [Estructura del proyecto](#estructura-del-proyecto)
8. [Convención de commits](#convención-de-commits)

---

## Requisitos

- **Python 3.10** o superior
- **pip**
- **Git**
- **MySQL Server**

---

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu-usuario/Backend-Harmony-SPA.git
   cd Backend-Harmony-SPA
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. Instalar las dependencias del proyecto:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

---

## Configuración

1. Crear un archivo `.env` en la raíz del proyecto basándose en el archivo de ejemplo `.env.example`:

   ```env
   APP_NAME=Harmony-SPA-API
   DEBUG=True
   DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/harmony_spa_db
   SECRET_KEY=tu_clave_secreta_aqui
   ```

2. Asegurar que el servicio de MySQL Server esté activo y la base de datos `harmony_spa_db` esté creada.

---

## Migraciones de Base de Datos

Este proyecto utiliza migraciones de base de datos gestionadas (por ejemplo, Alembic). Para aplicar las migraciones pendientes:

```bash
alembic upgrade head
```

---

## Ejecución

Para iniciar el servidor de desarrollo local con Uvicorn:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en `http://127.0.0.1:8000`. Puedes acceder a la documentación interactiva (Swagger UI) en `http://127.0.0.1:8000/docs`.

---

## Pruebas

Para ejecutar las pruebas automatizadas (con `pytest`):

```bash
pytest
```

---

## Estructura del proyecto

```text
Backend-Harmony-SPA/
│
├── alembic/              # Migraciones de base de datos
├── app/
│   ├── api/              # Endpoints y rutas de FastAPI
│   ├── domain/           # Entidades y lógica de dominio
│   ├── infrastructure/   # Conexión a BD y repositorios externos
│   ├── models/           # Modelos ORM (SQLAlchemy)
│   ├── schemas/          # Esquemas de validación y serialización (Pydantic)
│   ├── services/         # Lógica de negocio
│   └── main.py           # Punto de entrada de la aplicación
│
├── .env                  # Variables de entorno locales
├── requirements.txt      # Dependencias de Python
└── README.md             # Documentación del proyecto
```

---

## Convención de commits

Este proyecto sigue la especificación de **Conventional Commits**:

- `feat:` Nueva característica o funcionalidad.
- `fix:` Corrección de un error (bug).
- `docs:` Cambios exclusivos en la documentación.
- `style:` Cambios en formato, espacios, punto y coma, etc. (sin afectar código).
- `refactor:` Refactorización de código que no corrige bugs ni añade características.
- `test:` Adición o corrección de pruebas.
- `chore:` Tareas de mantenimiento, actualización de dependencias, etc.

Ejemplo: `docs(readme): actualizar estructura y migraciones bd`
