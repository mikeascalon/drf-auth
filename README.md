# LAB - Class 31

Project: Django REST Framework & Docker
Author: 

## Overview

Use Django REST Framework to create an API, then “containerize” it with Docker.

PORT - [Port Number](http://127.:8000/api/v1/coffees/)

### Running the Application

1. **Docker**: To run the application using Docker, ensure Docker is installed on your machine. Then execute:

```bash
docker-compose up --build
```

#### How to Use the API

Access the list of coffees or create a new coffee entry:

GET and POST requests to http://127.0.0.1:8000/api/v1/coffees/

Retrieve, update, or delete a specific coffee entry:

GET, PUT, PATCH, and DELETE requests to http://127.0.0.1:8000/api/v1/coffees/