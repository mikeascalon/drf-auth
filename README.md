# LAB - Class 33

Project: Authentication & Production Server

Author: Michelangelo Ascalon

## Overview

This project enhances an existing API by adding JWT Authentication to ensure secure access to resources. Additionally, it transitions the development server to Gunicorn, a production-grade WSGI server, for improved performance and scalability. The project also includes configuration for Docker to simplify deployment and development workflows.

### Setup

Prerequisites

1. Docker and Docker Compose installed on your machine.

2. Basic understanding of Docker, Django, and Django REST Framework.
   
#### Installation

1.Clone the repository to your local machine.

2. Navigate to the project directory.

3.Build and start the containers with Docker Compose.

```bash
docker-compose up --build

```

#### Access and Testing

The API is accessible at: http://127.0.0.1:8000/api/v1/coffees/

Using the API

* Get Tokens: POST request to `/api/token/` with username and password to receive access and refresh JWT tokens.
  
* Refresh Tokens: POST request to `/api/token/refresh/` with refresh token to receive a new access token.

CRUD Operations for Coffees Resource:

* Create (Token Required): POST to `/api/v1/coffees/` with coffee details.
  
* Read List: GET `/api/v1/coffees/` to retrieve a list of coffees.
  
* Read Detail: GET `/api/v1/coffees/<id>/` to retrieve coffee details.
  
* Update (Token Required): PUT or PATCH `/api/v1/coffees/<id>/` with updated coffee details.
  
* Delete (Token Required): DELETE `/api/v1/coffees/<id>/`.

bash

PORT - [Port Number](http://127.0.0.1:8000/api/v1/coffees/)

Manual Testing
Manual testing can be done using tools like httpie or ThunderClient, . Below are examples of how to manually test the endpoints:

```bash
# Get Tokens
http POST http://127.0.0.1:8000/api/token/ username=<username> password=<password>

# Refresh Token
http POST http://127.0.0.1:8000/api/token/refresh/ refresh=<refresh_token>

# Access Protected Route
http GET http://127.0.0.1:8000/api/v1/coffees/ "Authorization:Bearer <access_token>"

```
Replace <username>, <password>, <refresh_token>, and <access_token> with actual values

##### Notes

* Ensure Docker is running on your machine before starting the application.
  
* Adjust docker-compose.yml according to your database preference (SQLite or PostgreSQL).

* Static files are served using Whitenoise; ensure your static file paths are correctly set in settings for production.