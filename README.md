Todo Backend Django 


1. Install Django & Django REST Framework

    pip install django djangorestframework

 2. Create Project & App

    django-admin startproject todoproject
    cd todoproject
    python manage.py startapp todo

 3. Make Migrations


    python manage.py makemigrations
    python manage.py migrate

 4. Folder Structure

    todoproject/
    │
    ├── todo/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── views.py      <-- task_api is defined here
    │   ├── urls.py       <-- import from views
    │   └── migrations/
    │
    ├── todoproject/
    │   └── settings.py
    │
    └── manage.py

5. Enable Django CORS
    
    Install CORS headers on the Django side:
    pip install django-cors-headers

6. Test API with Postman

    POST /api/tasks/ - Add a task with title, due_date, due_time, and status (Pending by default).

    GET /api/tasks/ - Get the list of tasks with due_date, due_time, and status.

    PUT /api/tasks/<id>/ - Update a task's status and other fields.

    DELETE /api/tasks/<id>/ - Delete a task.

    Example POST data to add a task:


    {
        "title": "Buy groceries",
        "due_date": "2025-04-16",
        "due_time": "15:30:00",
        "status": "Pending"
    }


7. Run Server

    python manage.py runserver