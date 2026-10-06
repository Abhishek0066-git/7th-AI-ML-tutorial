# Program mein:

# Student ka naam print karo.
# Current skills print karo.
# "Azure" add karo.
# "React" add karo.
# Total skills print karo.
# Check karo "Python" available hai ya nahi.
# Skills ko alphabetical order mein sort karo.
# Final skills print karo.

student_name = "Abhishek"

skills = ["Python", "SQL", "Git"]
print(student_name)
print(skills)
skills.append("Azure")
skills.append("React")
print(skills)
print(len(skills))
print("Python" in skills)
skills.sort()
print(skills)
