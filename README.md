# LAB - Class 32

Project: Permissions & Postgresql

Author: Michelangelo Ascalon

## Overview

Added permissions to ensure that only authenticated users have access to the API. Implement a custom permission to allow only appropriate users to update or delete entries. Added functionality to switch users directly from the browsable API, enhancing the user experience and testing capabilities. Incorporate PostgreSQL in your Docker setup. 


PORT - [Port Number](http://127.0.0.1:8000/api/v1/coffees/)

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