from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test():
    return {"message" : "Hello, World!"}

@app.get("/hari")
def mantra():
    return "hare krishna hare krishna krishna krishna hare hare"

@app.get("/math")
def math():
    a = 5
    b = 7
    return a*b 


students = {1 : "nimai", 2 : "hari", 3 : "radhika"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{stud_id}")
def student_search(stud_id:int):
    return {"id" : stud_id, "name" : students[stud_id]}

@app.get("/add_student/{stud_id}/{name}")
def add_student(stud_id : int, name:str):
    students[stud_id] = name
    return students

@app.get("/add_student")
def add_student(stud_id : int, name:str):
    students[stud_id] = name
    return students

@app.post("/add_student_diff")
def add_student_diff():
    students["new_id"] = "new_name"
    return students


from pydantic import BaseModel

class newdata(BaseModel):
    stud_id : int
    name : str

@app.post("/add_student_new_value")
def  add_student_new_value(newdata:newdata):
    students[newdata.stud_id] = newdata.name
    return students












