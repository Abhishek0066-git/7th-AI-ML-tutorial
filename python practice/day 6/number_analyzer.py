numbers = [10, 15, 22, 7, 30, 41, 50]

# Program mein:

# Saare numbers print karo.
# Total numbers count karo.
# Saare even numbers print karo.
# Saare odd numbers print karo.
# Numbers ka total sum calculate karo.
# 20 se greater numbers print karo.

# Bonus ⭐
# Loop use karke largest number find karne ki try karo.

for num in numbers:
    print(num)

count =len(numbers)
print(count)

for num in numbers:
    if(num%2==0):
        print(num)

for num in numbers:
    if(num%2!=0):
        print(num)

total = 0
for num in numbers:
    total += num
print(total)

for num in numbers:
    if(num>20):
        print(num)

largest = numbers[0]
for num in numbers:
    if (num>largest):
        largest= num
print(largest)
