# gestor_tareas

Django app that implements a simple task manager, part of the `django_mastery` project.

## App contents

- **Model** (`models.py`): `Tarea` with the fields `titulo` (CharField), `descripcion` (TextField, optional), `completado` (BooleanField, defaults to `False`) and `fecha_creacion` (DateTimeField, set automatically on creation).
- **Form** (`forms.py`): `TareaForm`, a `ModelForm` based on `Tarea` with the `titulo` and `descripcion` fields.
- **Views** (`views.py`): `lista_tareas` — on `POST` it validates and saves a new task (redirects after saving); on `GET` it lists all tasks ordered by creation date (newest first) and renders the template.
- **Templates** (`templates/gestor_tareas/`):
  - `lista.html` — extends `blog_estatico/base.html`; shows the task creation form and the list of tasks with their status (completed/pending).
- **Routes** (`urls.py`):

  | Route | View | Description |
  |-------|------|-------------|
  | `''` | `lista_tareas` | Task list and creation of new tasks |

- **Admin** (`admin.py`): `Tarea` registered with `list_display` showing `titulo`, `completado` and `fecha_creacion`.

## Usage

This app is part of the `django_mastery` Django project and does not run standalone.
It must be registered in `INSTALLED_APPS` and its routes included in the project's root `urls.py`
(already configured under the `tareas/` prefix). To start the server, run from the repository root:

```bash
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/tareas/`.
