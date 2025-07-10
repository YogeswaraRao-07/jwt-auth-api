# JWT Authentication API

A Django REST Framework-based API that uses JWT for authentication. Dockerized and deployable on AWS EC2.

## API Endpoints

POST /api/auth/login/
Request Body
{
  "username": "admin",
  "password": "admin123"
}

Response
{
  "token": "JWT_TOKEN",
  "expires": "2025-07-10T07:17:55Z"
}

POST /api/auth/verify/
Request Body

{
  "token": "JWT_TOKEN"
}

Response

{
  "valid": true,
  "message": "Token is valid"
}

GET /api/auth/validate/
Header

Authorization: Bearer JWT_TOKEN
Response

{
  "valid": true,
  "user": "admin",
  "expires": "2025-07-10T07:17:55Z"
}

# Login
  POST http://<YOUR-EC2-IP>:8000/api/auth/login/ \
    "Content-Type: application/json" \
    '{"username":"admin", "password":"admin123"}'

# Verify Token
  POST http://<YOUR-EC2-IP>:8000/api/auth/verify/ \
    "Content-Type: application/json" \
    '{"token":"<JWT>"}'

# Validate Token
  GET http://<YOUR-EC2-IP>:8000/api/auth/validate/ \
    "Authorization: Bearer <JWT>"

Technologies Used

Python, Django, Django REST Framework
JWT (PyJWT)
Docker & Docker Compose
AWS EC2 (Ubuntu)

Sample Credentials:
Username: admin
Password: admin123
