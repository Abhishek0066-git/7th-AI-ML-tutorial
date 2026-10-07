# Student ka name input lo
# City input lo
# Skill input lo
# Information student.txt mein save karo
# File ko read karo
# Saved information print karo
# ⭐ Bonus: second skill bhi save karo

with open("student.txt" , "w") as file:
    file.write(input("Student name:" )+ "\n")
    file.write(input("City: " )+"\n")
    file.write(input("Skill: " )+"\n")

with open("student.txt", "r") as file:
    reads = file.readlines()
    print(reads)
with open("student.txt", "a") as file:
    file.write(input("skill_2: ")+"\n")

with open("student.txt", "r") as file:
    print(file.read())
