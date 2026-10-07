# Task 1 — Create & Write
file = open("data.txt", "w")
file.write("Abhishek\n")
file.write("Python\n")
file.write("AI/ML\n")
file.close()

# Task 2 — Read
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# Task 3 — Append
with open("data.txt", "a") as file:
    file.write("\nSQL")
    file.write("\nPython")

# Task 4 — Read Lines
with open("data.txt", "r") as file:
    lines = file.readlines()
print(lines)

# Task 5 — Read One Line
with open("data.txt", "r") as file:
    line = file.readline()
print(line)

# Task 6 — Loop
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)

# Task 7 — Count Lines ⭐
with open("data.txt","r") as file:
    lines = file.readlines()
print("number of lines in the file: ", len(lines))

# Task 8 — Search ⭐
with open("data.txt", "r") as file:
    found = False
    for line in file:
        if"Python"in line:
            found = True
    if found is True:
        print("Python is found")
    else:
        print("Python is not found")
        
        
