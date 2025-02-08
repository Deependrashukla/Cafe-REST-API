# Cafe Management System API

This is a Flask-based REST API for managing users and items in a cafe management system. The API interacts with a SQL Server database using the `pyodbc` library. It supports CRUD operations for users and items, authentication via JWT, and is containerized using Docker for easy deployment.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Directory Structure](#directory-structure)
4. [Setup Instructions](#setup-instructions)
5. [API Endpoints](#api-endpoints)
6. [Database Schema](#database-schema)
7. [Deployment with Docker](#deployment-with-docker)
8. [Dependencies](#dependencies)
9. [Security Considerations](#security-considerations)
10. [Contributing](#contributing)
11. [License](#license)

---

## Overview
The **Cafe Management System API** allows you to manage users and items in a cafe. It uses Flask for the backend, `pyodbc` for database interaction, and JWT for authentication. The API is designed to be scalable and can be deployed using Docker.

---

## Features
- **User Management**:
  - Register new users.
  - Authenticate users with username and password.
  - Retrieve user details by ID.
  - Delete users by ID.
- **Item Management**:
  - Add, retrieve, update, and delete items.
  - Fetch all items or a specific item by ID.
- **JWT Authentication**:
  - Secure endpoints using JSON Web Tokens (JWT).
  - Logout functionality invalidates tokens.
- **Docker Support**:
  - Containerized application for easy deployment.

---

## Directory Structure
```
project-folder/
├── Dockerfile                # Docker configuration for containerization
├── requirements.txt          # Python dependencies
├── db/
│   ├── itemdb.py             # Database interactions for items
│   └── usersdb.py            # Database interactions for users
├── schemas.py                # Data validation schemas
├── app.py                    # Main Flask application
└── README.md                 # This file
```

---

## Setup Instructions

### Prerequisites
1. **Python 3.10+**: Install Python from [python.org](https://www.python.org/).
2. **SQL Server**: Ensure you have a SQL Server instance running with the `cafe` database.
3. **Docker**: Install Docker from [docker.com](https://www.docker.com/).

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Deependrashukla/Cafe-REST-API.git
   cd cafe-management-api
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**:
   - Create a SQL Server database named `cafe`.
   - Create the following tables:
     ```sql
     CREATE TABLE users (
         id INT PRIMARY KEY IDENTITY(1,1),
         username NVARCHAR(50) NOT NULL UNIQUE,
         password NVARCHAR(255) NOT NULL
     );

     CREATE TABLE item (
         id NVARCHAR(50) PRIMARY KEY,
         name NVARCHAR(100) NOT NULL,
         price FLOAT NOT NULL
     );
     ```

4. **Update Database Connection**:
   - Open `db/usersdb.py` and `db/itemdb.py`.
   - Update the connection string in the `pyodbc.connect()` method to match your SQL Server configuration:
     ```python
     self.conn = pyodbc.connect(
         'DRIVER={SQL Server};SERVER=your_server_name;DATABASE=cafe;', timeout=30
     )
     ```

5. **Run the Application**:
   ```bash
   flask run
   ```
   The API will be available at `http://localhost:5000`.

---

## API Endpoints

### User Endpoints
| Method | Endpoint       | Description                          | Requires Auth |
|--------|----------------|--------------------------------------|---------------|
| POST   | `/user`        | Register a new user                  | No            |
| GET    | `/user?id=<id>`| Get user details by ID               | Yes           |
| DELETE | `/user?id=<id>`| Delete a user by ID                  | Yes           |
| POST   | `/login`       | Authenticate user and generate token | No            |
| POST   | `/logout`      | Log out user (invalidate token)      | Yes           |

### Item Endpoints
| Method | Endpoint           | Description                     | Requires Auth |
|--------|--------------------|---------------------------------|---------------|
| GET    | `/item`            | Get all items                   | Yes           |
| GET    | `/item?id=<id>`    | Get item details by ID          | Yes           |
| POST   | `/item`            | Add a new item                  | Yes           |
| PUT    | `/item?id=<id>`    | Update an item                  | Yes           |
| DELETE | `/item?id=<id>`    | Delete an item by ID            | Yes           |

---

## Database Schema

### `users` Table
| Column    | Type         | Description                  |
|-----------|--------------|------------------------------|
| `id`      | INT          | Unique identifier for the user |
| `username`| NVARCHAR(50) | Username (unique)            |
| `password`| NVARCHAR(255)| Hashed password              |

### `item` Table
| Column    | Type         | Description                  |
|-----------|--------------|------------------------------|
| `id`      | NVARCHAR(50) | Unique identifier for the item |
| `name`    | NVARCHAR(100)| Name of the item             |
| `price`   | FLOAT        | Price of the item            |

---

## Deployment with Docker

### Build the Docker Image
```bash
docker build -t cafe-api .
```

### Run the Docker Container
```bash
docker run -p 5005:5000 cafe-api
```
- Access the API at `http://localhost:5005`.

---

## Dependencies
- **Flask**: Web framework for building APIs.
- **Flask-Smorest**: Adds Swagger/OpenAPI documentation to Flask.
- **Flask-JWT-Extended**: Handles JWT-based authentication.
- **pyodbc**: Connects to SQL Server databases.
- **SQL Server ODBC Driver**: Required for `pyodbc` to interact with SQL Server.

---

## Security Considerations
1. **SQL Injection**:
   - Use parameterized queries instead of string interpolation to prevent SQL injection.
2. **Password Hashing**:
   - Hash passwords using a secure algorithm like `bcrypt` before storing them in the database.
3. **Environment Variables**:
   - Store sensitive information (e.g., database credentials) in environment variables.
4. **Token Expiration**:
   - Set an expiration time for JWT tokens to enhance security.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
