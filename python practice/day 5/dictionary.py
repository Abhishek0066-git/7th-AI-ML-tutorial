# Task 1 — Basic Dictionary

from asyncio import Task


student = {
    "name": "abhishek",
    "age": 25,
    "city": "Gurgaon",
    "course": "AI/ML"
}
print(student["name"])
print(student["age"])
print(student["city"])
print(student["course"])

# Task 2 — Change value
student["age"]= 26
print(student["age"])

# Task 3 — Add data
student["language"]= "Python"
print(student["language"])

# Task 4 — get()

print(student.get("name"))
print(student.get("language"))
print(student.get("salary"))

# Task 5 — Membership
print("name" in student)
print("skills" in student)

# Task 6 — Delete
del student["course"]
print(student)

# Task 7 — keys(), values(), items()
print(student.keys())
print(student.values())
print(student.items())

# Task 8 — Loop

skills = {
    "language": "Python",
    "database": "SQL",
    "cloud": "Azure",
    "version_control": "Git"
}

for key, value in skills.items():
    print(key,"," ,value)
