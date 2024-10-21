# DRF Blog API with JWT Authentication

This project is a Django Rest Framework (DRF) application that provides a complete Blog API with JWT authentication, permission management, and detailed API documentation using **Swagger**.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

## Features

### 1. **JWT Authentication**
- Secure user authentication using **JWT** (JSON Web Tokens).
- Endpoints for login, token refresh, and token verification.
- JWT tokens required for accessing protected routes.

### 2. **Blog CRUD Operations**
- **Create**, **Read**, **Update**, and **Delete** blog posts.
- Only the author of a post can edit or delete it.
  
### 3. **Permissions**
- Custom permission classes restrict access:
  - **IsAuthenticatedOrReadOnly**: Authenticated users can create/update posts.
  - **IsOwnerOrReadOnly**: Only the post owner can modify or delete a post.

### 4. **ViewSets**
- ViewSets handle CRUD operations for blog posts and user profiles.
- Examples:
  - `BlogPostViewSet`: Manages blog posts.

### 5. **Generic Views**
- DRF's generic views provide customizable endpoints for specific tasks.
- Example: `CreateAPIView` is used for user registration.

### 6. **Schema Generation and API Documentation**
- **Swagger** and **ReDoc** auto-generate API documentation.
  - Accessible via `/swagger/` and `/redoc/`.


## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set up the database:

```bash
python manage.py migrate
```

### 4. Run the development server:

```bash
python manage.py runserver
```

### 5. Access the API:
- The API is accessible at `http://127.0.0.1:8000/`.
- Swagger UI can be accessed at `http://127.0.0.1:8000/swagger/`.

## Usage

### Register a new user:

```bash
POST /api/users/register/
```

### Get a JWT token:

```bash
POST /api/token/
```

### Access a protected route with the JWT token:

```bash
Authorization: Bearer <your_token>
```

## Technologies Used

- **Django**: High-level web framework.
- **Django Rest Framework (DRF)**: For building the REST API.
- **Django Rest Framework Simple JWT**: For handling JWT authentication.
- **drf-yasg**: For auto-generating Swagger and ReDoc API documentation.
