skills = ["Python", "SQL", "Git", "Azure", "React"]

# task 1
# Print:

# First skill
# Third skill
# Last skill
# Total skills



print(skills[0])
print(skills[2])
print(skills[-1])
print(len(skills))

# Task 2 — Slicing
#Isi list se:

# 1. First 3 skills
# 2. Last 2 skills
# 3. Middle 3 skills

# print karo.

print(skills[0:3])
print(skills[-2:])
print(skills[1:4])

# Task 3 - Modifying Lists

languages = ["Python", "C++", "Java"]
languages[1]= "JavaScript"

print(languages[1])

# Task 4 — Add Items

skills = ["Python", "SQL"]

skills.append("Git")
skills.insert(1, "Azure")
print(skills)

# Task 5 — Remove

skills = ["Python", "SQL", "Git", "Azure"]
skills.remove("SQL")
skills.pop()
print(skills)

# Task 6 — Search
skills = ["Python", "SQL", "Git", "Azure"]
print("Python" in skills)
print("java" in skills)

# Task 7 — Numbers
numbers = [45, 12, 78, 3, 29, 10]
numbers.sort()
numbers.reverse()
print(numbers)
total_num = len(numbers)
print(total_num)

# Task 8 — Count & Index
numbers = [10, 20, 10, 30, 10, 40]
count_10 = numbers.count(10)
print(count_10)
print(numbers.index(30))
