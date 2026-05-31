## School Backend API

A backend API built with FastAPI to manage core school data, including students, teachers, and events. 
The project is structured using modular routers to ensure scalability, maintainability, and clean separation of concerns.
                                                                
Features
RESTful API built with FastAPI
Modular architecture using routers
Alumnos (Students management)
Docentes (Teachers management)
Eventos (School events management)
JSON-based communication
Automatic API documentation with Swagger UI
Easy to extend for additional modules (grades, attendance, etc.)
Tech Stack
Python
FastAPI
Uvicorn (ASGI server)
Pydantic (data validation)
Database integration (postgreSQL)

Project Structure

app/
│
├── main.py
├── models/
├── database/
│                             
└── routers/
   ├── alumnos.py
   ├── docentes.py
   └── eventos.py


Installation
Clone the repository:
git clone https://github.com/your-username/school-backend-api.git

Move into the project directory:
cd school-backend-api

Create a virtual environment (recommended):
python -m venv venv

source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

Install dependencies:
pip install fastapi uvicorn

Running the Server

Start the development server using Uvicorn:
uvicorn main:app --reload

The API will be available at:
Base URL: http://127.0.0.1:8000
Swagger Docs: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

API Modules:
Alumnos (Students)
Handles student-related operations such as:
Create student
Get student list
Update student information
Delete student

Docentes (Teachers)
Handles teacher-related operations such as:
Register teacher
List teachers
Update teacher data
Remove teacher

Eventos (Events)
Manages school events:
Create event
View upcoming events
Update event details
Delete events

Example Endpoint
GET /alumnos/

Response:

[
  {
    "nombre": "Juan Pérez",
    "grado": "3B",
    "edad": "14",
  }
]

Future Improvements
Add authentication (JWT)
Role-based access (admin, teacher, student)
Add attendance and grading modules
Deploy using Docker
License

This project is for educational purposes.
