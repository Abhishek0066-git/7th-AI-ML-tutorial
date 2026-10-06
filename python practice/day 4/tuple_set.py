# task 1 Tuple 
skills = ("Python", "SQL", "Git", "Azure", "React")
print(skills[0])
print(skills[2])
print(skills[-1])
print(len(skills))

# Task 2 — Tuple slicing
print(skills[0:3])
print(skills[-2:])
print(skills[1:4])

# Task 3 — Tuple methods
numbers = (10, 20, 10, 30, 10, 40)
print(numbers.count(10))
print(numbers.index(30))

# Task 4 — Set duplicates
skills = {"Python", "SQL", "Python", "Git", "SQL", "Azure"}
print(skills)

# Task 5 — Set add
skills = {"Python", "SQL", "Git"}
skills.add("Azure")
skills.add("React")
print(skills)

# Task 6 — Set remove
skills = {"Python", "SQL", "Git", "Azure"}
skills.remove("SQL")
print(skills)

# Task 7 — Membership
skills = {"Python", "SQL", "Git"}
print("Python" in skills)
print("Java" in skills)
