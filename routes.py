from fastapi import APIRouter, HTTPException
from models import Student
from database import get_connection

router = APIRouter()

@router.get("/students") # TODO: Replace ??? with correct endpoint path
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM students")

    row = cursor.fetchall()

    students = []

    count = 0
    
    for i in range(len(row)):
        students.append(row[i])
        count += 1
        
    conn.commit()
    conn.close()

    return {
        "students": students,
        "count": count,
    }
    
@router.get("/students/by-major") # TODO: Replace ??? with correct endpoint path
def get_students_by_major(major: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM students WHERE major = '{major}'")

    row = cursor.fetchall()

    names = []

    count = 0

    for i in range(len(row)):
        if row[i][3] == major:
            names.append(row[i][1])
            count += 1

    conn.commit()
    conn.close()

    return {
        "name": names,
        "count": count,
        "major": major,
    }
    
@router.get("/students/by-gpa") # TODO: Replace ??? with correct endpoint path
def get_students_by_gpa(min_gpa: float):
    
    if min_gpa < 0.0 or min_gpa > 4.0:
        raise HTTPException(status_code = 400, detail = f"GPA must be between 0.0 and 4.0")
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM students WHERE gpa >= {min_gpa}")

    row = cursor.fetchall()

    count = 0

    names = []
    
    for i in range(len(row)):
        if row[i][4] >= min_gpa:
            names.append(row[i][1])
            count += 1

    conn.commit()
    conn.close()

    return {
        "name": names,
        "count": count,
        "major": min_gpa,
    }
    
@router.get("/student/{student_id}") # TODO: Replace ??? with correct endpoint path
def get_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    if not cursor.execute(f"SELECT * FROM students WHERE id = {student_id}").fetchone():
        raise HTTPException(status_code = 404, detail = f"Student with ID {student_id} not found")

    cursor.execute(f"SELECT * FROM students WHERE id = {student_id}")

    row = cursor.fetchone()

    student_name = row[1]
    student_email = row[2]
    student_major = row[3]
    student_gpa = row[4]
    student_enrollment = row[5]
    

    conn.commit()
    conn.close()

    return {
        "id": student_id,
        "name": student_name,
        "email": student_email,
        "major": student_major,
        "gpa": student_gpa,
        "enrollment_year": student_enrollment
    } 

    
@router.post("/students", status_code=201) # TODO: Replace ??? with correct endpoint path
def create_student(student: Student):
    conn = get_connection()
    cursor = conn.cursor()

    if student.gpa < 0.0 or student.gpa > 4.0:
        raise HTTPException(status_code = 400, detail = "GPA must be between 0.0 and 4.0")

    elif not student.name or not student.name.strip():
        raise HTTPException(status_code = 400, detail = "Name field is empty, put in a name")

    elif not student.major or not student.major.strip():
        raise HTTPException(status_code = 400, detail = "Major field is empty, put in a major")

    cursor.execute("INSERT INTO students (name, email, major, gpa, enrollment_year)" f"VALUES ('{student.name.strip()}', '{student.email}', '{student.major.strip()}', {student.gpa}, {student.enrollment_year})")

    row = cursor.fetchone()
    
    conn.commit()
    conn.close()
    
    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "major": student.major,
        "gpa": student.gpa,
        "enrollment_year": student.enrollment_year
    }
    
    
@router.put("/students/{student_id}") # TODO: Replace ??? with correct endpoint path
def update_student(student_id: int, student: Student):
    conn = get_connection()
    cursor = conn.cursor()

    if not cursor.execute(f"SELECT * FROM students WHERE id = {student_id}").fetchone():
        raise HTTPException(status_code = 404, detail = f"Student with ID {student_id} not found")

    elif student.gpa < 0.0 or student.gpa > 4.0:
        raise HTTPException(status_code = 400, detail = "GPA must be between 0.0 and 4.0")

    elif not student.name or not student.name.strip():
        raise HTTPException(status_code = 400, detail = "Name field is empty, put in a name")

    elif not student.major or not student.major.strip():
        raise HTTPException(status_code = 400, detail = "Major field is empty, put in a major")

    cursor.execute(
           f"UPDATE students SET name = '{student.name.strip()}', email = '{student.email}', major = '{student.major.strip()}', gpa = {student.gpa}, enrollment_year = {student.enrollment_year} WHERE id = {student_id}")

    row = cursor.fetchone()
    
    conn.commit()
    conn.close()
    
    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "major": student.major,
        "gpa": student.gpa,
        "enrollment_year": student.enrollment_year
    } 
    
@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    if not cursor.execute(f"SELECT * FROM students WHERE id = {student_id}").fetchone():
        raise HTTPException(status_code = 404, detail = f"Student with ID {student_id} not found")

    cursor.execute(f"DELETE FROM students WHERE id = {student_id}")

    conn.commit()
    conn.close()

    return {"message": "Student deleted successfully"}