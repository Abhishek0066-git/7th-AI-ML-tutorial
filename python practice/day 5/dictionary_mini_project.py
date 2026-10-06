student = {
    "name": "Abhishek",
    "age": 25,
    "city": "Gurgaon",
    "skills": ["Python", "SQL", "Git"]
}

# Program mein:

# Student name print karo.
# Age print karo.
# City print karo.
# Skills print karo.
# "Azure" skills mein add karo.
# Age 26 karo.
# "course": "AI/ML" add karo.
# Check karo "Python" skills mein available hai ya nahi.
# Dictionary ke all keys print karo.
# Final student profile print karo.
print(student["name"])
print(student["age"])
print(student["city"])
print(student["skills"])
student["skills"].append("Azure")
student["age"]=26
student["course"]= "AI/ML"
print("Python" in student["skills"])
print(student.keys())
print(student)