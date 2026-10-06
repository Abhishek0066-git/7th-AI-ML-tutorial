# Function 1
def print_student_name(student):
    print(student["name"])

# Function 2
def count_skills(student):
    return len(student["skills"])

# Function 3
def has_python(student):
    return "Python" in student["skills"]




student = {
    "name": "Abhishek",
    "age": 25,
    "skills": ["Python", "SQL", "Git"]
}
print_student_name(student)
print(f"Number of skills: {count_skills(student)}")
print(f"Has Python skill: {has_python(student)}")
