# gestor_tareas

App de Django que implementa un gestor de tareas simple, dentro del proyecto `django_mastery`.

## Contenido de la app

- **Modelo** (`models.py`): `Tarea` con los campos `titulo` (CharField), `descripcion` (TextField, opcional), `completado` (BooleanField, por defecto `False`) y `fecha_creacion` (DateTimeField, asignada automáticamente al crear).
- **Formulario** (`forms.py`): `TareaForm`, un `ModelForm` sobre `Tarea` con los campos `titulo` y `descripcion`.
- **Vistas** (`views.py`): `lista_tareas` — en `POST` valida y guarda una nueva tarea (redirige tras guardar); en `GET` lista todas las tareas ordenadas por fecha de creación descendente y renderiza la plantilla.
- **Plantillas** (`templates/gestor_tareas/`):
  - `lista.html` — extiende `blog_estatico/base.html`; muestra el formulario de alta y el listado de tareas con su estado (completada/pendiente).
- **Rutas** (`urls.py`):

  | Ruta | Vista | Descripción |
  |------|-------|-------------|
  | `''` | `lista_tareas` | Listado de tareas y alta de nuevas tareas |

- **Admin** (`admin.py`): `Tarea` registrado con `list_display` mostrando `titulo`, `completado` y `fecha_creacion`.

## Uso

Esta app forma parte del proyecto Django `django_mastery` y no se ejecuta de forma independiente.
Debe estar registrada en `INSTALLED_APPS` y sus rutas incluidas en el `urls.py` raíz del proyecto
(ya configurado bajo el prefijo `tareas/`). Para levantar el servidor, ejecuta desde la raíz del repositorio:

```bash
python manage.py runserver
```

Luego visita `http://127.0.0.1:8000/tareas/`.
