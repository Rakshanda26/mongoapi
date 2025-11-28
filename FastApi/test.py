from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

db_url =""
class students(BaseModel):
    id : int 
    name : str
    age : int 


def save_student_to_file(data):
    with open("student.txt", "a") as f:
        f.write(f"{data.id}, {data.age}, {data.name}\n")


def get_connection_url():
    conn =psycopg2.connect(db_url, cursor_factory=RealDictCursor)
    return conn


@app.post("/students")
def create_student(stud : students):
    save_student_to_file(stud)
    return {"message" : "students data saved successfully"}


@app.post("/student/db/insert")
def store_student_db(student :students):
    conn = get_connection_url()
    cursor = conn.cursor()
    insert_query = "INSERT INTO student (id, name, age) values (%s, %s, %s)"
    cursor.execute(insert_query, (student.id, student.name,student.age))
    conn.commit()
    cursor.close()
    conn.close()


@app.put("/student/db/update")
def update_student_db(student: students):
    conn = get_connection_url()
    cursor = conn.cursor()

    update_query = "UPDATE student SET name = %s, age = %s WHERE id = %s"
    cursor.execute(update_query, (student.name, student.age, student.id))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Student updated successfully"}


@app.delete("/student/db/delete/{student_id}")
def delete_student_db(student_id: int):
    conn = get_connection_url()
    cursor = conn.cursor()

    delete_query = "DELETE FROM student WHERE id = %s"
    cursor.execute(delete_query, (student_id,))

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Student deleted successfully"}
