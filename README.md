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


# Setup

## 1. Clone the Repository

```bash
git clone https://github.com/KRATOS9810/healthcare-backend-system
cd healthcare-backend-system
```

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Create the PostgreSQL Database

Create a PostgreSQL database named:

```text
healthcare
```

Make sure PostgreSQL is running.

## 5. Configure Environment Variables

Create a `.env` file in the project root.

Use `.env.example` as a reference:

```env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthcare
DB_USER=postgres
DB_PASSWORD=your-postgres-password
DB_HOST=localhost
DB_PORT=5432
```

Replace the database credentials with your own PostgreSQL credentials.

Do not commit the `.env` file to GitHub.

## 6. Run Migrations

```bash
python manage.py migrate
```

## 7. Create an Admin User

```bash
python manage.py createsuperuser
```

Follow the prompts to create the admin account.

## 8. Start the Server

```bash
python manage.py runserver
```

The backend will be available at:

```text
http://127.0.0.1:8000/
```

---

# How to Use the API

The API can be used with Postman, a frontend application, mobile application, or any REST API client.

All URLs below assume the server is running at:

```text
http://127.0.0.1:8000
```

---

## Step 1: Register an Account

Create a user account.

**POST**

```text
/api/auth/register/
```

Request:

```json
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "Password123!"
}
```

Example response:

```json
{
    "name": "John Doe",
    "email": "john@example.com"
}
```

---

## Step 2: Login

After registering, log in to receive JWT tokens.

**POST**

```text
/api/auth/login/
```

Request:

```json
{
    "email": "john@example.com",
    "password": "Password123!"
}
```

Example response:

```json
{
    "refresh": "<refresh-token>",
    "access": "<access-token>"
}
```

Copy the `access` token.

---

## Step 3: Authenticate API Requests

Patient, doctor, and mapping endpoints require authentication.

In Postman:

```text
Authorization → Bearer Token
```

Paste the JWT `access` token.

Alternatively, add this HTTP header:

```text
Authorization: Bearer <access-token>
```

The access token must be included with all protected API requests.

---

# Patient API

## Step 4: Create a Patient

**POST**

```text
/api/patients/
```

Request:

```json
{
    "name": "John Doe",
    "age": 35,
    "gender": "Male",
    "phone": "9876543210",
    "address": "Delhi"
}
```

The response contains the patient's ID.

Save the patient ID because it will be needed when creating a patient-doctor mapping.

---

## Step 5: List Patients

**GET**

```text
/api/patients/
```

Returns the patients created by the currently authenticated user.

---

## Step 6: Get a Patient

**GET**

```text
/api/patients/<id>/
```

Example:

```text
/api/patients/1/
```

---

## Step 7: Update a Patient

**PUT**

```text
/api/patients/<id>/
```

Example:

```text
/api/patients/1/
```

Request:

```json
{
    "name": "John Updated",
    "age": 36,
    "gender": "Male",
    "phone": "9876543210",
    "address": "Noida"
}
```

---

## Step 8: Delete a Patient

**DELETE**

```text
/api/patients/<id>/
```

Example:

```text
/api/patients/1/
```

---

# Doctor API

## Step 9: Create a Doctor

**POST**

```text
/api/doctors/
```

Request:

```json
{
    "name": "Dr. Sharma",
    "specialization": "Cardiology",
    "phone": "9123456789",
    "email": "doctor@example.com"
}
```

Save the doctor ID from the response.

---

## Step 10: List Doctors

**GET**

```text
/api/doctors/
```

Returns doctors available to authenticated users.

---

## Step 11: Get a Doctor

**GET**

```text
/api/doctors/<id>/
```

Example:

```text
/api/doctors/1/
```

---

## Step 12: Update a Doctor

**PUT**

```text
/api/doctors/<id>/
```

Example:

```text
/api/doctors/1/
```

Request:

```json
{
    "name": "Dr. Sharma Updated",
    "specialization": "Neurology",
    "phone": "9123456789",
    "email": "doctor@example.com"
}
```

---

## Step 13: Delete a Doctor

**DELETE**

```text
/api/doctors/<id>/
```

Example:

```text
/api/doctors/1/
```

---

# Patient-Doctor Mapping API

A mapping connects a patient with a doctor.

A patient can have multiple doctors, and a doctor can be assigned to multiple patients.

---

## Step 14: Assign a Doctor to a Patient

Use the patient ID and doctor ID obtained from the previous requests.

**POST**

```text
/api/mappings/
```

Request:

```json
{
    "patient": 1,
    "doctor": 1
}
```

For example, if:

```text
Patient ID = 2
Doctor ID  = 5
```

send:

```json
{
    "patient": 2,
    "doctor": 5
}
```

---

## Step 15: List All Mappings

**GET**

```text
/api/mappings/
```

Returns the patient-doctor mappings associated with patients belonging to the authenticated user.

---

## Step 16: View Doctors Assigned to a Patient

**GET**

```text
/api/mappings/<patient_id>/
```

Example:

```text
/api/mappings/2/
```

This means:

> Get all doctors assigned to patient ID 2.

---

## Step 17: Delete a Mapping

**DELETE**

```text
/api/mappings/<mapping_id>/
```

Example:

```text
/api/mappings/5/
```

This deletes mapping ID `5`.

### Important

The mapping endpoints use the same URL structure for two different operations:

```text
GET    /api/mappings/<patient_id>/
DELETE /api/mappings/<mapping_id>/
```

The HTTP method determines what the ID represents.

---

# API Endpoint Summary

## Authentication

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/api/auth/register/` | Register a user | No |
| POST | `/api/auth/login/` | Login and receive JWT tokens | No |

## Patients

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/api/patients/` | Create patient | Yes |
| GET | `/api/patients/` | List user's patients | Yes |
| GET | `/api/patients/<id>/` | Get patient | Yes |
| PUT | `/api/patients/<id>/` | Update patient | Yes |
| DELETE | `/api/patients/<id>/` | Delete patient | Yes |

## Doctors

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/api/doctors/` | Create doctor | Yes |
| GET | `/api/doctors/` | List doctors | Yes |
| GET | `/api/doctors/<id>/` | Get doctor | Yes |
| PUT | `/api/doctors/<id>/` | Update doctor | Yes |
| DELETE | `/api/doctors/<id>/` | Delete doctor | Yes |

## Mappings

| Method | Endpoint | Description | Auth |
|---|---|---|---|
| POST | `/api/mappings/` | Assign doctor to patient | Yes |
| GET | `/api/mappings/` | List mappings | Yes |
| GET | `/api/mappings/<patient_id>/` | Get patient's mappings | Yes |
| DELETE | `/api/mappings/<mapping_id>/` | Delete mapping | Yes |

---

# Validation and Permissions

## Authentication

Patient, doctor, and mapping endpoints require JWT authentication.

Unauthenticated requests return:

```text
401 Unauthorized
```

## Patient Access

Users can only access patients they created.

For example:

```text
User A
 ├── Patient A
 └── Patient B

User B
 └── Patient C
```

User A cannot access User B's Patient C.

User B cannot access User A's Patient A or Patient B.

## Mapping Access

Users cannot create mappings using another user's patient.

For example:

```text
User A owns Patient A

User B attempts:
POST /api/mappings/

{
    "patient": <Patient A ID>,
    "doctor": 1
}
```

This request is rejected because User B does not own the patient.

## Patient Validation

- Age must be between `0` and `150`.
- Phone number must contain only digits.
- Phone number must contain exactly `10` digits.

## Doctor Validation

- Phone number must contain only digits.
- Phone number must contain exactly `10` digits.
- Email addresses are validated using Django's `EmailField`.

## Duplicate Mappings

The same doctor cannot be assigned to the same patient more than once.

Duplicate mappings are prevented using serializer validation and a database-level unique constraint.

---

# Django Admin

Django provides a built-in administration interface.

Start the server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

Log in using the superuser created with:

```bash
python manage.py createsuperuser
```

The admin interface can be used to manage:

- Users
- Patients
- Doctors
- Patient-doctor mappings

The Django Admin is used for backend administration and is separate from the REST API.

---

# Testing

The API can be tested using Postman or another REST API client.

Recommended testing flow:

1. Register a user.
2. Login and obtain a JWT access token.
3. Add the access token as a Bearer token.
4. Create a patient.
5. Create a doctor.
6. Assign the doctor to the patient.
7. Retrieve patients, doctors, and mappings.
8. Update patient and doctor records.
9. Delete records.
10. Test invalid input.
11. Test duplicate mappings.
12. Create a second user.
13. Verify that the second user cannot access another user's patients.
14. Verify that the second user cannot create mappings using another user's patients.

---

# Project Validation

Run:

```bash
python manage.py check
```

Expected result:

```text
System check identified no issues (0 silenced).
```

---

# Environment and Security

Sensitive configuration is stored in environment variables.

The following files are excluded from Git:

```text
.env
venv/
__pycache__/
*.pyc
```

The repository contains `.env.example` as a reference for the required environment variables.

Never commit real database passwords, secret keys, or other sensitive credentials to the repository.


