
Techforing Project Management API
=================================

A simple **RESTful API** built with **Django** and **Django REST Framework** for managing users, projects, tasks, and comments.

Features
--------

*   **User Management**: Register, log in, and manage users.
    
*   **Project Management**: Create, update, and delete projects.
    
*   **Task Management**: Add tasks, assign them to users, and track progress.
    
*   **Comment System**: Add comments to tasks for collaboration.
    
*   **Authentication**: Token-based authentication for secure access.
    
*   **Documentation**: API documentation using Swagger and ReDoc.
    

Installation
------------

1.  Clone the repository:
    
    
        git clone https://github.com/mostafagafer/Techforing.git
    
2.  Navigate to the project directory:
    
    
        cd Techforing
    
3.  Set up a virtual environment and install dependencies:
    
    
        python -m venv venv
        source venv/bin/activate  # On Windows: venv\Scripts\activate
        pip install -r requirements.txt
    
4.  Run migrations and start the server:
    
    
        cd project_management
        python manage.py makemigraion
        python manage.py migrate
        python manage.py runserver
    

API Endpoints
-------------

### Users

*   **Register User**: POST `/api/users/register/`
    
    
        {
          "username": "testuser",
          "email": "test@example.com",
          "password": "securepassword123"
        }
    
*   **Login User**: POST `/api/users/login/`
    
    
        {
          "username": "testuser",
          "password": "securepassword123"
        }
    

### Projects

*   **List Projects**: GET `/api/projects/`
    
*   **Create Project**: POST `/api/projects/`
    
    
        {
          "name": "New Project",
          "description": "This is a new project."
        }
    

### Tasks

*   **List Tasks**: GET `/api/projects/{project_id}/tasks/`
    
*   **Create Task**: POST `/api/projects/{project_id}/tasks/`
    
    
        {
          "title": "New Task",
          "description": "This is a new task.",
          "status": "To Do",
          "priority": "High",
          "assigned_to": 1,
          "due_date": "2023-12-31T23:59:59Z"
        }
    

### Comments

*   **List Comments**: GET `/api/tasks/{task_id}/comments/`
    
*   **Create Comment**: POST `/api/tasks/{task_id}/comments/`
    
    
        {
          "content": "This is a new comment."
          "task": 2
        }
    

Usage
-----

1.  **Register a new user** using the `/api/users/register/` endpoint.
    
2.  **Log in** using the `/api/users/login/` endpoint to get an authentication token.
    
3.  **Use the token in the Authorization header** for authenticated requests:
    
    
        Authorization: Token <your_token_here>
    
4.  **Create projects, tasks, and comments** using the respective endpoints.
    

Documentation
-------------

*   **Swagger UI**: Access the API documentation at `/swagger/`.
    
*   **ReDoc**: Access the API documentation at `/redoc/`.
    

Contributing
------------

Feel free to contribute to this project by submitting pull requests or opening issues.



Acknowledgment
--------------

A big shout-out to DeepSeek for helping me create this project from scratch. Thanks to the AI community for making these tools available and inspiring countless possibilities.

* * *

### Notes

*   Ensure you have the necessary dependencies installed (`django`, `djangorestframework`, `drf-yasg`, etc.).
    
*   Make sure to run the migrations before starting the server.
    
*   Use the provided Swagger and ReDoc endpoints for detailed API documentation.
    

* * *
