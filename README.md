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
