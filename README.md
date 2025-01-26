# Techforing Project Management API
A simple **RESTful API** built with **Django** and **Django REST Framework** for managing users, projects, tasks, and comments.

## Features
- **User Management**: Register, log in, and manage users.
- **Project Management**: Create, update, and delete projects.
- **Task Management**: Add tasks, assign them to users, and track progress.
- **Comment System**: Add comments to tasks for collaboration.
- **Authentication**: Token-based authentication for secure access.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mostafagafer/Techforing.git
2. Navigate to the project directory:
   ```bash
   cd Techforing
3. Set up a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
4. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver

## API Endpoints
API Endpoints
Users
Register User: POST /api/users/register/

json
Copy
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword123"
}
Login User: POST /api/users/login/

json
Copy
{
  "username": "testuser",
  "password": "securepassword123"
}
Projects
List Projects: GET /api/projects/

Create Project: POST /api/projects/

json
Copy
{
  "name": "New Project",
  "description": "This is a new project."
}
Tasks
List Tasks: GET /api/projects/{project_id}/tasks/

Create Task: POST /api/projects/{project_id}/tasks/

json
Copy
{
  "title": "New Task",
  "description": "This is a new task.",
  "status": "To Do",
  "priority": "High",
  "assigned_to": 1,
  "due_date": "2023-12-31T23:59:59Z"
}
Comments
List Comments: GET /api/tasks/{task_id}/comments/

Create Comment: POST /api/tasks/{task_id}/comments/

json
Copy
{
  "content": "This is a new comment."
}
Usage
Register a new user using the /api/users/register/ endpoint.

Log in using the /api/users/login/ endpoint to get an authentication token.

Use the token in the Authorization header for authenticated requests:

Copy
Authorization: Token <your_token_here>
Create projects, tasks, and comments using the respective endpoints.


