# Employee Management System

A Python-based Employee Management System with a Streamlit user interface and a FastAPI backend.

## 1. Project Overview

The Employee Management System is a small web application for managing employee records. It provides a Streamlit interface that communicates with a FastAPI backend through HTTP requests.

## 2. Problem Statement

Managing employee details manually can make it harder to add, view, find, update, and remove employee records. This project demonstrates a simple application that brings these basic employee-management operations into one interface.

## 3. Objectives

- Build a simple interface for employee-management operations.
- Create REST API endpoints for employee records.
- Connect the frontend to the backend using HTTP requests.
- Practise Python application development with FastAPI and Streamlit.

## 4. Technologies Used

- **Python** — application programming language
- **FastAPI** — backend API framework
- **Pydantic** — request-data validation
- **Streamlit** — frontend user interface
- **Requests** — HTTP communication between frontend and backend
- **Uvicorn** — ASGI server used to run the FastAPI application

## 5. Key Features

- **Dashboard:** Displays the total number of employees and reports whether the backend connection succeeds.
- **Add Employee:** Adds an employee with an ID, name, department, salary, and optional email.
- **View Employees:** Displays the employee list in a table.
- **Update Employee:** Updates an existing employee record.
- **Search Employee:** Finds an employee using the employee ID.
- **Delete Employee:** Removes an employee using the employee ID.

## 6. Project Structure

```text
Employee_Management_System/
├── backend/
│   └── main.py
├── frontend/
│   └── app.py
├── requirements.txt
├── .gitignore
└── .gitattributes
```

## 7. How the Application Works

1. The user selects an operation in the Streamlit frontend.
2. The frontend sends an HTTP request to the FastAPI backend.
3. FastAPI processes the request and returns a response.
4. Streamlit displays the result to the user.

The frontend currently sends requests to `http://127.0.0.1:8000`.

## 8. Setup and Run

### Prerequisites

- Python installed
- pip package installer

### Install dependencies

Open a terminal in the project root folder:

```bash
py -m pip install -r requirements.txt
```

### Start the backend

Open a terminal:

```bash
cd backend
py -m uvicorn main:app --reload
```

The API runs locally at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### Start the frontend

Open a **second terminal** in the project root folder:

```bash
cd frontend
py -m streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser.

## 9. Results and Outcomes

The project code provides a single interface for the six employee-management operations listed above, with the Streamlit frontend communicating with the FastAPI backend.

## 10. Key Learnings

- Building REST API endpoints with FastAPI
- Validating request data with Pydantic
- Creating a user interface with Streamlit
- Sending HTTP requests with the Requests library
- Connecting a frontend application to a backend API
- Organising a Python project into frontend and backend folders

## 11. Current Implementation Notes

- Employee records are currently stored in an in-memory Python list in the backend. They are not persisted in a database, so records reset when the backend process restarts.
- The backend includes three initial sample employee records. Replace sample data with appropriate test data before demonstrations.
- The frontend is configured to connect to the backend at `http://127.0.0.1:8000`.
- This repository contains the source code; publishing it to GitHub does not by itself host or deploy the application online.

## 12. Repository

GitHub: https://github.com/banutejap363-ai/Employee_Management_System

## 13. Screenshots and Demo

Add screenshots of the running application and a demo video link here when they are ready.

## 14. Hashtags

#Python #FastAPI #Streamlit #EmployeeManagementSystem #RESTAPI #GitHub #SoftwareDevelopment
