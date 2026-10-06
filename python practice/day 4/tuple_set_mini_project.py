student_name = "Abhishek"

skills = ["Python", "SQL", "Python", "Git", "SQL", "Azure"]

# Program mein:

# Student name print karo.
# Current skills print karo.
# List ko set mein convert karo.
# Unique skills print karo.
# React add karo.
# SQL remove karo.
# Check karo Python available hai ya nahi.
# Total unique skills print karo.
# Important 🔥

print(student_name)
print(skills)
skills_set= set(skills)
print(skills_set)
skills_set.add("React")
skills_set.remove("SQL")
print("Python" in skills_set)
print(len(skills_set))

# IMPORTENT 🔥

# List   → changeable + duplicates allowed
# Tuple  → cannot change
# Set    → unique values + duplicates removed
