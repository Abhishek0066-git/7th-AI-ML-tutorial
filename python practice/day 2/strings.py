# task 1 
name = "Abhishek"
print(name[0])
print(name[2])
print(name[-1])
print(len(name))

# task 2
print(name[1:4])
print(name[2:6])
print(name[:4])
print(name[4:])

# task 3
print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("Abhishek", "abhi"))

# task 4
name1 = "Abhishek"
city = "Gurgaon"
age = 20

details = "my name is" + " " + name1 + " and i am from " + city + " and my age are "+ str(age)
print(details)

print(f"my name is {name1} and i am from {city} and my age are{age}")

# task 5
name3 = "Abhishek Kumar Gupta "
print("Kumar" in name3)
print("kumar" in name3)
print("Gupta" in name3)
print("python" in name3)

# task 6
text = " python is powerful "
print(text.strip())
print(text.split())
print(" ".join(text.split()))


# task-7
print("Name:\tAbhishek\nCity:\tGurgaon\nLanuage:\tpython")

# task 8

email = "abhishek@gmail.com"
print(email.startswith("abhishek"))
print(email.endswith("gmail.com"))
print(email.endswith("yahoo.com"))

# task 9
text = "python programming is easy and python is powerful"
print(text.count("python"))
print(text.find("programming"))
print(text.find("java"))

# task 10
text1 = "Python"
text2 = "12345"
text3 = "Python123"
text4 = "Python 123"
print(text1.isalpha())
print(text1.isdigit())
print(text1.isalnum())

print(text2.isalpha())
print(text2.isdigit())
print(text2.isalnum())

print(text3.isalpha())
print(text3.isdigit())
print(text3.isalnum())

print(text4.isalpha())
print(text4.isdigit())
print(text4.isalnum())