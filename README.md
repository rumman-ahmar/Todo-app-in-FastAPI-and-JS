# Todo App in FastAPI and JS

This project is a simple Todo application developed using FastAPI (Python) for backend API endpoints and JavaScript for frontend functionality. The application allows users to manage a list of Todo items.

## Project Structure
- database/
  - database.py: Contains the configuration for the database used in the project
  - models.py: Defines the models used within the project, representing the structure of the data
  - schema.py: Contains Pydantic schema for validating and serializing/deserializing data models
- static/
  - main.js: JavaScript file handling frontend functionalities of the application
- templates/
  - index.html: HTML file that forms the structure and layout of the frontend of the application
- main.py: Contains the configuration for FastAPI, including API routes, HTML serving, and other necessary settings

## Setup and Installation
1. Clone repository
```
git clone https://github.com/rumman-ahmar/Todo-app-in-FastAPI-and-JS.git
```
2. Install Dependencies
```
pip install -r requirements.txt
```

## Running the Application
1. Start the FastAPI Server:
```
uvicorn main:app --reload
```
2. Access the Application:
  - Open a web browser and navigate to http://localhost:8000 or the URL specified in the terminal after starting the FastAPI server
  - You should see the Todo application interface where you can interact with Todo items

## Usage
- The application interface will display a list of Todo items
- Users can add new Todo items, update existing ones, and delete completed tasks
- The frontend functionality is implemented using JavaScript (main.js) to interact with the FastAPI backend endpoints

## Demo
![Recording 2023-12-21 042508](https://github.com/rumman-ahmar/Todo-app-in-FastAPI-and-JS/assets/72764336/251a76e1-f47f-48e8-8fcb-5beb54b47146)
