name = input("Enter your name")
age = int(input("Enter your age"))

if(age >= 18 and age <= 60):
    print(name, "is eligible")
else:
    print(name, "is not eligible")