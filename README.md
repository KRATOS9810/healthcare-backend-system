# Healthcare Backend System

A RESTful healthcare backend built with Django REST Framework and PostgreSQL.

The system provides JWT-based authentication and APIs for managing patients, doctors, and patient-doctor mappings.

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- psycopg2
- python-dotenv

## Features

- User registration and JWT authentication
- Patient management
- Doctor management
- Patient-doctor mapping
- Authentication-protected APIs
- User-specific patient access
- Input validation
- Duplicate mapping prevention
- PostgreSQL database integration
- Django Admin interface

## Project Structure

```text
healthcare_backendsystem/
│
├── accounts/       # User registration and authentication
├── patients/       # Patient APIs
├── doctors/        # Doctor APIs
├── mappings/       # Patient-doctor mapping APIs
├── config/         # Django project configuration
├── manage.py
├── requirements.txt
├── .env.example
└── .gitignore
```


## Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd healthcare_backendsystem
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows CMD:**

```cmd
venv\Scripts\activate
```

**Windows PowerShell:**

```powershell
venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create the environment file

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

> Do not commit your `.env` file. It contains sensitive information.

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create a superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 8. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## API Authentication

This project uses JWT authentication.

### Obtain tokens

Send a POST request to:

```text
/api/token/
```

with:

```json
{
    "username": "your_username",
    "password": "your_password"
}
```

The response contains an access token and refresh token.

### Authenticate requests

Use the access token in the Authorization header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

### Refresh an expired access token

Send the refresh token to:

```text
/api/token/refresh/
```

## Useful Commands

Start the server:

```bash
python manage.py runserver
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

