# 📝 Django Todo API Backend

A simple and clean RESTful Todo API built using **Django** and **Django REST Framework**.

## 📦 Installation

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/todo-backend.git
cd todo-backend
Create a Virtual Environment & Install Dependencies


python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install django djangorestframework django-cors-headers

** Start Project and App **

django-admin startproject todoproject
cd todoproject
python manage.py startapp todo


** Add to INSTALLED_APPS in settings.py: **


INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'todo',
]


** CORS Setup in settings.py: **


MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # For development


** Run Migrations **

python manage.py makemigrations
python manage.py migrate

** Run Server **

python manage.py runserver

🗂️ Folder Structure



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


🧪 Test API with Postman
➕ Add Task
POST /api/tasks/
Body:


{
  "title": "Buy groceries",
  "due_date": "2025-04-16",
  "due_time": "15:30:00",
  "status": "Pending"
}
📃 Get All Tasks
GET /api/tasks/

🔁 Update Task
PUT /api/tasks/<id>/
Body:


{
  "title": "Buy vegetables",
  "due_date": "2025-04-17",
  "due_time": "16:00:00",
  "status": "Completed"
}

❌ Delete Task
DELETE /api/tasks/<id>/


🛠️ Built With

Django

Django REST Framework

django-cors-headers