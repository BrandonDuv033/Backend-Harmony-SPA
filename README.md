# Backend-Harmony-SPA

API backend construida con **FastAPI**. Este repositorio sirve como espacio de práctica para aplicar FastAPI sobre una arquitectura por capas.

> **Estado:** en exploración. El alcance funcional del proyecto aún está por definirse.

<!-- TODO: cuando se defina el objetivo, reemplazar este bloque con 2-3 frases sobre qué problema resuelve y para quién. -->

---

## Tabla de contenido

1. [Requisitos](#requisitos)
2. [Instalación](#instalación)
3. [Configuración](#configuración)
4. [Ejecución](#ejecución)
5. [Pruebas](#pruebas)
6. [Estructura del proyecto](#estructura-del-proyecto)
7. [Convención de commits](#convención-de-commits)

---

## Requisitos

- Python 3.10 o superior
- pip
- Git

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Backend-Harmony-SPA
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Linux / macOS
   source venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración

Las variables de entorno se manejan con un archivo `.env` (no se sube al repositorio).

1. Copiar la plantilla:

   ```bash
   cp .env.example .env
   ```

2. Completar los valores en `.env` según el entorno.

## Ejecución

Levantar el servidor en modo desarrollo:

```bash
uvicorn app.main:app --reload
```

Una vez en marcha, FastAPI genera la documentación automáticamente:

| Recurso | URL |
|---|---|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

## Pruebas

```bash
pytest
```

Actualmente existe una prueba de salud (`test/test_health.py`) que verifica que la API responde.

## Estructura del proyecto

```
Backend-Harmony-SPA/
├── app/
│   ├── api/              # Routers y endpoints
│   ├── core/             # Configuración y elementos centrales
│   ├── domain/           # Lógica y reglas del dominio
│   ├── infrastructure/   # Conexiones externas (base de datos, servicios)
│   ├── models/           # Modelos de datos
│   ├── repositories/     # Acceso a datos
│   ├── schemas/          # Esquemas de validación (Pydantic)
│   ├── services/         # Lógica de negocio
│   ├── utils/            # Funciones de apoyo
│   ├── __init__.py
│   └── main.py           # Punto de entrada de la aplicación
├── scripts/              # Scripts de utilidad
├── test/                 # Pruebas automatizadas
├── .env.example          # Plantilla de variables de entorno
├── .gitignore
├── README.md
└── requirements.txt
```

## Convención de commits

Se recomienda usar commits semánticos:

| Prefijo | Uso |
|---|---|
| `feat:` | Nueva funcionalidad |
| `fix:` | Corrección de errores |
| `docs:` | Cambios en documentación |
| `test:` | Pruebas |
| `refactor:` | Reestructuración sin cambiar comportamiento |
| `chore:` | Tareas de mantenimiento |

Ejemplo: `docs: agregar README inicial del proyecto`

---