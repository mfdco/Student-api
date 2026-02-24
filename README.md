REST API HOMEWORK ASSIGNMENT

1.) Project Description
   ---------------------
This project contains a REST API used to manage and create student records using FAST API and SQLite.It allows the user to create, retrieve, delete, or update student information in the database. The purpose of this project is to better understand how APIs work along with how they can be used with a databse. 

=========================================================================

2.) Installation Instructions
    --------------------------
Step 1 : Clone the repository and cd into the file
	a.) git clone <https://github.com/mfdco/Student-api.git>
	b.) cd student-api

Step 2 : Create a virtual environment
	a.) python -m venv .venv
	b.1) source .venv/bin/activate (Mac/Linux)
	b.2) .venv\Scripts\activate (Windows)

Step 3 : Install requirements
	a.) pip install -r requirements.txt

Step 4 : Start up FASTAPI
	a.) uvicorn mail:app --reload

Step 5 : Click on the webstite's url
	a.) Copy and paste http://127.0.0.1.8000 into a url
	b.) add /docs to the end of the url to enter into the API documentation and test the API

=========================================================================

3.) API endpoints
   --------------- 
 Method | Endpoint        | Description                 | Codes
________|_________________|_____________________________|______ 
  GET   |/student         |gets all students            |200
  GET   |/student/{id}    |get specific student by id   |200, 404
  GET   |/student/by-major|get specific student by major|200
  GET   |/student/by-gpa  |get specific student by gpa  |200, 404
  POST  |/studen          |create student               |201, 400
  PUT   |/student/{id}    |update student               |200, 400, 404
 DELETE |/student/{id}    |delete student               |200/204, 404

=========================================================================

4.) Testing instructions
   ----------------------
Step 1 : Start server
	a.) refer to Running Server

Step 2 : Test the api within documentation
	a.) Start with create student 
	b.) Use the other endpoints the modify, get, or delete the student record(s)

========================================================================= 

5.) Examples

Example 1 (Create Student) :
  
	curl -X 'POST' \ 
	  'http://127.0.0.1:8000/students' \ 
	  -H 'accept: application/json' \ 
	  -H 'Content-Type: application/json' \ 
	  -d '{ 
	  "id": 0, 
	  "name": "Lee Roy", 
	  "email": "leyroy8@gmail.com", 
	  "major": "Business Administration", 
	  "gpa": 3.1, 
	  "enrollment_year": 1 
        }'

Example 2 (Get all students) :
 
	curl -X 'GET' \
  	  'http://127.0.0.1:8000/students' \
  	  -H 'accept: application/json'

Example 3 (Get one student by id) : 
	
	curl -X 'GET' \
  	  'http://127.0.0.1:8000/student/1' \
  	  -H 'accept: application/json'

=========================================================================
