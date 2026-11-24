# 🔷 Backend-Harmony-SPA

**API REST para la gestión del sistema Harmony Spa**

Desarrollada con **FastAPI**, utilizando una arquitectura por capas que facilita la organización, el mantenimiento y la escalabilidad del proyecto.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?style=flat-square&logo=fastapi&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-yellow?style=flat-square)

</p>

---

## 📖 Descripción

Backend desarrollado con **FastAPI** para la gestión del sistema Harmony Spa, implementando una **arquitectura por capas** que permite separar responsabilidades, facilitar el mantenimiento y mejorar la escalabilidad de la aplicación.

La arquitectura contempla los siguientes componentes:

- **Domain:** entidades y reglas del negocio.
- **Infrastructure:** conexión a base de datos e infraestructura externa.
- **API:** endpoints y rutas de FastAPI.
- **Models:** modelos ORM.
- **Schemas:** validación y serialización de datos.
- **Services:** lógica de negocio.
- **Repositories:** acceso y gestión de datos.

### 🚧 Estado del proyecto

![Fase 3](https://img.shields.io/badge/Fase%203-Autenticación%20y%20Persistencia-blue?style=flat-square)

**Fase 3: Autenticación y persistencia de datos**

Actualmente, el proyecto cuenta con:

- Hashing y verificación de contraseñas mediante **Argon2id**.
- Inicialización del único usuario `SUPER_ADMIN`.
- Autenticación mediante tokens **JWT**.
- Gestión y revocación de sesiones en MySQL.
- Protección de rutas y control de inactividad.
- Implementación completa de los modelos ORM mediante **SQLAlchemy**.
- Definición de relaciones entre usuarios, perfiles, procedimientos y reservas.
- Migraciones de base de datos gestionadas con **Alembic**.

---

## 📑 Tabla de contenido

1. [Requisitos](#-requisitos)
2. [Instalación](#-instalación)
3. [Configuración](#️-configuración)
4. [Migraciones de base de datos](#️-migraciones-de-base-de-datos)
5. [Modelos ORM y persistencia](#️-modelos-orm-y-persistencia)
6. [Inicialización del SuperAdmin](#-inicialización-del-superadmin)
7. [Autenticación y gestión de sesiones](#-autenticación-y-gestión-de-sesiones)
8. [Ejecución](#️-ejecución)
9. [Pruebas](#-pruebas)
10. [Estructura del proyecto](#-estructura-del-proyecto)
11. [Convención de commits](#-convención-de-commits)

---

## 📋 Requisitos

Antes de comenzar, asegúrate de contar con las siguientes herramientas:

| Herramienta  | Requisito                           |
| :----------- | :---------------------------------- |
| Python       | 3.10 o superior                     |
| pip          | Gestor de paquetes de Python        |
| Git          | Control de versiones                |
| MySQL Server | Sistema de gestión de base de datos |

---

## ⚙️ Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local.

**1. Clonar el repositorio**

```bash
git clone https://github.com/tu-usuario/Backend-Harmony-SPA.git
cd Backend-Harmony-SPA
```

**2. Crear y activar el entorno virtual**

```bash
python -m venv venv
```

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Actualizar pip e instalar las dependencias**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Entre las dependencias utilizadas para la seguridad y autenticación se encuentran:

- `pwdlib[argon2]`: generación y verificación de hashes de contraseñas mediante Argon2id.
- `PyJWT`: generación y validación de tokens JWT.

---

## 🛠️ Configuración

**1. Crear el archivo `.env`**

En la raíz del proyecto, crea un archivo `.env` tomando como referencia `.env.example`.

**2. Configurar las variables de entorno**

Ejemplo de configuración:

```env
APP_NAME=Harmony-SPA-API
DEBUG=True

DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/harmony_spa_db

SECRET_KEY=tu_clave_secreta_aqui
```

La configuración de seguridad también contempla parámetros relacionados con JWT:

- **Clave de firma:** utilizada para firmar y validar los tokens.
- **Algoritmo:** define el algoritmo utilizado para la firma JWT.
- **Expiración:** establece un límite de 30 minutos de inactividad para las sesiones.

Estos parámetros se encuentran centralizados en `app/core/config.py` y documentados en `.env.example`.

**3. Configurar la base de datos**

- Verificar que el servicio de MySQL Server esté activo.
- Crear la base de datos `harmony_spa_db`.
- Comprobar que las credenciales configuradas en `.env` sean correctas.

> ⚠️ **Importante:** No compartas el archivo `.env` ni subas credenciales o claves secretas al repositorio.

---

## 🗄️ Migraciones de base de datos

El proyecto utiliza **Alembic** para gestionar las migraciones de la base de datos, permitiendo mantener sincronizados los modelos de la aplicación con la estructura de MySQL.

**Aplicar las migraciones pendientes:**

```bash
alembic upgrade head
```

Este comando ejecuta todas las migraciones pendientes hasta alcanzar la última versión disponible.

---

## 🔐 Inicialización del SuperAdmin

El proyecto contempla un único usuario con el rol `SUPER_ADMIN`, encargado de representar el nivel principal de administración del sistema.

La inicialización se realiza mediante un script de consola, sin disponer de un endpoint público para esta operación.

### 1. Verificar el módulo de seguridad

Las funciones `hash_password` y `verify_password`, ubicadas en:

```text
app/core/security.py
```

Permiten:

- Generar hashes seguros mediante Argon2id.
- Verificar contraseñas comparándolas con sus hashes almacenados.

### 2. Ejecutar el script de inicialización

Desde la raíz del proyecto, ejecuta:

```bash
python -m scripts.create_super_admin
```

El script solicitará los datos necesarios para registrar al administrador principal.

### 3. Validaciones de seguridad

Durante el proceso se aplican las siguientes condiciones:

- El correo electrónico debe tener un formato válido.
- Las contraseñas deben coincidir.
- La contraseña debe contener al menos 12 caracteres.
- La contraseña se almacena mediante hashing Argon2id.

### 4. Restricción de unicidad

La base de datos restringe la existencia de más de un usuario con el rol `SUPER_ADMIN`.

Por lo tanto, este proceso está diseñado exclusivamente para inicializar el administrador principal del sistema.

---

## 🗃️ Modelos ORM y persistencia

El proyecto utiliza **SQLAlchemy ORM** para representar las entidades del sistema y gestionar su persistencia en MySQL.

La capa de modelos contempla las siguientes entidades:

### 1. Enumeraciones de dominio

Se implementó `AppointmentStatus` en `app/domain/enums/appointment_status.py`, encargado de controlar los estados del ciclo de vida de las reservas:

| Estado | Descripción |
|:--|:--|
| `PENDIENTE` | Reserva pendiente de confirmación. |
| `CONFIRMADA` | Reserva confirmada. |
| `EN_PROCESO` | Procedimiento en ejecución. |
| `COMPLETADA` | Procedimiento finalizado. |
| `CANCELADA` | Reserva cancelada. |
| `NO_ASISTIO` | El cliente no asistió. |

### 2. Modelos del sistema

| Modelo | Responsabilidad |
|:--|:--|
| `User` | Información principal de los usuarios. |
| `UserSession` | Registro y control de sesiones. |
| `ClientProfile` | Información adicional de los clientes. |
| `EmployeeProfile` | Información laboral de los empleados. |
| `Procedure` | Catálogo de procedimientos y servicios. |
| `ProcedureSession` | Sesiones programadas de cada procedimiento. |
| `Appointment` | Gestión de citas y reservas. |

### 3. Relaciones y restricciones

Se implementaron relaciones entre las entidades para mantener la integridad de los datos:

- **User – ClientProfile:** relación uno a uno (1:1).
- **User – EmployeeProfile:** relación uno a uno (1:1).
- **Appointment:** vincula al cliente, procedimiento y esteticista asignada.
- **Procedure – ProcedureSession:** permite definir las sesiones que componen un procedimiento.

También se incorporaron restricciones mediante `CheckConstraint`:

- Los precios de los procedimientos no pueden ser negativos.
- La duración de los procedimientos debe ser positiva.
- La fecha de finalización de una reserva debe ser posterior a su fecha de inicio.

### 4. Registro central de modelos

Todos los modelos se consolidan en:

```text
app/models/__init__.py
```

Esto permite centralizar su importación y garantizar que las siete tablas estén registradas en `Base.metadata`, facilitando su reconocimiento durante la generación de migraciones con Alembic.

### 5. Migraciones

Se generó y aplicó la migración correspondiente para crear las nuevas tablas y relaciones en MySQL.

Para aplicar futuras migraciones pendientes:

```bash
alembic upgrade head
```

## 🔑 Autenticación y gestión de sesiones

El sistema implementa un mecanismo de autenticación basado en **JSON Web Tokens (JWT)**, permitiendo identificar usuarios, validar sus sesiones y proteger los endpoints de la API.

### 1. Esquemas de autenticación

Se implementaron esquemas mediante **Pydantic** para validar los datos de entrada y salida:

| Esquema         | Archivo               | Función                                                                  |
| :-------------- | :-------------------- | :----------------------------------------------------------------------- |
| `LoginRequest`  | `app/schemas/auth.py` | Validar las credenciales de inicio de sesión.                            |
| `TokenResponse` | `app/schemas/auth.py` | Estructurar la respuesta con el token.                                   |
| `UserResponse`  | `app/schemas/user.py` | Retornar el perfil público del usuario sin exponer información sensible. |

Los esquemas se exportan centralizadamente desde `app/schemas/__init__.py`.

### 2. Servicio de autenticación

El archivo `app/services/auth_service.py` centraliza la lógica de autenticación y gestión de sesiones.

Sus principales responsabilidades son:

- Validar las credenciales del usuario mediante Argon2id.
- Generar tokens JWT firmados.
- Registrar sesiones activas en MySQL.
- Gestionar la revocación de sesiones.

### 3. Protección de rutas

Se implementó la dependencia `get_current_user` en:

```text
app/api/dependencies.py
```

Esta dependencia permite:

- Validar la autenticidad del token recibido mediante el esquema Bearer.
- Identificar al usuario asociado a la sesión.
- Comprobar que el usuario continúe activo.
- Controlar la actividad de la sesión.
- Revocar sesiones que superen los 30 minutos de inactividad.

### 4. Endpoints de autenticación

Los endpoints se encuentran implementados en `app/api/v1/auth.py` e integrados mediante el router de la versión 1 de la API.

| Endpoint  | Método | Descripción                                   |
| :-------- | :----- | :-------------------------------------------- |
| `/login`  | POST   | Autenticar al usuario y generar un token JWT. |
| `/me`     | GET    | Obtener el perfil del usuario autenticado.    |
| `/logout` | POST   | Cerrar la sesión y revocar el token asociado. |

**Flujo general de autenticación:**

```text
       Usuario
          │
          ▼
   Enviar credenciales
          │
          ▼
        /login
          │
          ▼
 Validar contraseña
      (Argon2id)
          │
          ▼
   Generar token JWT
          │
          ▼
 Registrar sesión
      en MySQL
          │
          ▼
  Acceder a rutas
     protegidas
          │
          ▼
  get_current_user
          │
          ▼
 Validar usuario y
 estado de sesión
          │
          ▼
    Acceso permitido
```

**Nota:** La expiración por inactividad se controla mediante la validación de actividad de la sesión, con un límite de 30 minutos.

---

## ▶️ Ejecución

Para iniciar el servidor de desarrollo local, utiliza **Uvicorn**:

```bash
uvicorn app.main:app --reload
```

Una vez iniciado, la API estará disponible en las siguientes direcciones:

| Recurso    | URL                         |
| :--------- | :-------------------------- |
| API local  | http://127.0.0.1:8000       |
| Swagger UI | http://127.0.0.1:8000/docs  |
| ReDoc      | http://127.0.0.1:8000/redoc |

La documentación interactiva permite consultar y probar los endpoints disponibles.

---

## 🧪 Pruebas

El proyecto utiliza **Pytest** para ejecutar pruebas automatizadas.

Para ejecutar todas las pruebas:

```bash
pytest
```

---

## 📁 Estructura del proyecto

La organización general sigue una arquitectura por capas:

```text
Backend-Harmony-SPA/
│
├── alembic/                      # Migraciones de base de datos
│
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── auth.py            # Endpoints de autenticación
│   │   │   └── router.py          # Router principal de API v1
│   │   │
│   │   └── dependencies.py        # Dependencias de autenticación
│   │
│   ├── core/
│   │   ├── config.py              # Configuración centralizada
│   │   └── security.py            # Seguridad y hashing Argon2id
│   │
│   ├── domain/                    # Entidades y lógica de dominio
│   │   └── enums/
│   │       └── appointment_status.py  # Estados de las reservas
│   ├── infrastructure/            # Conexión a BD e infraestructura externa
│   ├── models/                    # Modelos ORM (SQLAlchemy)
│   │   ├── __init__.py                 # Registro central de modelos
│   │   ├── user.py                     # Usuario
│   │   ├── user_session.py             # Sesiones de usuario
│   │   ├── client_profile.py           # Perfil del cliente
│   │   ├── employee_profile.py         # Perfil del empleado
│   │   ├── procedure.py                # Procedimientos
│   │   ├── procedure_session.py        # Sesiones de procedimientos
│   │   └── appointment.py              # Citas y reservas
│   ├── schemas/
│   │   ├── auth.py                # Esquemas de autenticación
│   │   ├── user.py                # Esquemas de usuario
│   │   └── __init__.py            # Exportación centralizada
│   │
│   ├── services/
│   │   └── auth_service.py        # Servicio de autenticación
│   │
│   └── main.py                    # Punto de entrada de FastAPI
│
├── scripts/
│   └── create_super_admin.py      # Inicialización del SuperAdmin
│
├── .env                           # Variables de entorno locales
├── .env.example                   # Plantilla de configuración
├── requirements.txt               # Dependencias del proyecto
└── README.md                      # Documentación del proyecto
```

---

## 📝 Convención de commits

Este proyecto sigue la especificación **Conventional Commits**, utilizando los siguientes tipos:

| Tipo       | Descripción                                                                 |
| :--------- | :-------------------------------------------------------------------------- |
| `feat`     | Nueva característica o funcionalidad.                                       |
| `fix`      | Corrección de errores.                                                      |
| `docs`     | Cambios en la documentación.                                                |
| `style`    | Cambios de formato que no afectan la lógica.                                |
| `refactor` | Reestructuración del código sin añadir funcionalidades ni corregir errores. |
| `test`     | Adición o modificación de pruebas.                                          |
| `chore`    | Tareas de mantenimiento y actualización de dependencias.                    |

### Formato

```text
tipo(alcance): descripción breve
```

**Ejemplos:**

```bash
feat(auth): agregar hashing argon2id y superadmin
feat(auth): implementar autenticacion con jwt
docs(readme): actualizar documentacion de autenticacion
```

---

<p align="center">

**Backend-Harmony-SPA**

Desarrollado con Python, FastAPI y MySQL.

_Proyecto en desarrollo continuo._

</p>
