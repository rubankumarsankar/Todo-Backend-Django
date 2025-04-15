# 📝 Django Todo API Backend

A simple and clean RESTful Todo API built using **Django** and **Django REST Framework**.

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/todo-backend.git
cd todo-backend
Create a Virtual Environment & Install Dependencies
```

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django djangorestframework django-cors-headers
```

2. ** Start Project and App **

```bash
django-admin startproject todoproject
cd todoproject
python manage.py startapp todo
```

3. ** Add to INSTALLED_APPS in settings.py: **

```bash
INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'todo',
]
```

4. ** CORS Setup in settings.py: **

```bash
MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # For development

```

5. ** Run Migrations **
```bash
python manage.py makemigrations
python manage.py migrate
```
6. ** Run Server **

```bash
python manage.py runserver
```
7. 🗂️ Folder Structure

```bash

todoproject/
│
├── todo/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py         # task_api defined here
│   ├── urls.py          # import views here
│   └── migrations/
│
├── todoproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── manage.py

```

8. 🧪 Test API with Postman

➕ Add Task
POST /api/tasks/
Body:

```bash
{
  "title": "Buy groceries",
  "due_date": "2025-04-16",
  "due_time": "15:30:00",
  "status": "Pending"
}
```

📃 Get All Tasks
GET /api/tasks/

🔁 Update Task
PUT /api/tasks/<id>/
Body:

```bash
{
  "title": "Buy vegetables",
  "due_date": "2025-04-17",
  "due_time": "16:00:00",
  "status": "Completed"
}
``` 
❌ Delete Task
DELETE /api/tasks/<id>/


10. 🛠️ Built With

Django

Django REST Framework

django-cors-headers