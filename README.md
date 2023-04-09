# Server Monitoring Tool Backend
This repository contains the backend code for the Server Monitoring Tool. The backend is built using Django, a Python web framework, and provides RESTful API endpoints for the frontend app to communicate with.

## Requirements
1. Python 3.x
2. Django 3.x
3. Django REST framework

## Installation
1. Clone the repository to your local machine: ``` git clone https://github.com/Ikshan-Tango/hacklipse-backend ```
2. Install the required libraries: ``` pip install django djangorestframework```
3. Edit the configuration file `settings.py` with your database settings:```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'database_name',
        'USER': 'database_user',
        'PASSWORD': 'database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}```
4. Migrate the database: ```python manage.py migrate```
5. Create a superuser account: ```python manage.py createsuperuser```
6. Run the server: ```python manage.py runserver``` The server will be running on http://localhost:8000 by default.

