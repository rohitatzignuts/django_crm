# Django CRUD with PostgreSQL

This is a simple Django CRUD (Create, Read, Update, Delete) project using a PostgreSQL database.

## Features
- Create, Read, Update, and Delete records
- PostgreSQL as the database
- Django admin panel
- Bootstrap for basic UI styling

## Prerequisites
Make sure you have the following installed:
- Python (>=3.8)
- PostgreSQL
- pip and virtualenv

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/rohitatzignuts/django_crm.git
```

### 2. Set Up Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Configure PostgreSQL Database
Create a PostgreSQL database and update the `DATABASES` settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 6. Create a Superuser
```sh
python manage.py createsuperuser
```

### 7. Run the Server
```sh
python manage.py runserver
```
Access the app at `http://127.0.0.1:8000/`.

## Usage
- Navigate to the homepage to perform CRUD operations.
- Use the Django admin panel at `http://127.0.0.1:8000/admin/`.


