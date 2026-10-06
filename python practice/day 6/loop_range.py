# Task 1 — Basic for
for i in range(1,6):
    print(i)

# Task 2 — Reverse
for i in range(10, 4, -1):
    print(i)

# Task 3 — List loop
skills = ["Python", "SQL", "Git", "Azure"]
for skill in skills:
    print(skill)

# Task 4 — Even numbers
for i in range(2, 21, 2):
    print(i)  
    # or
for i in range(1, 21):
    if i%2 == 0:
        print(i)

# Task 5 — Odd numbers
for i in range(1, 21):
    if i%2 != 0:
        print(i)

# Task 6 — Sum
numbers = [10, 20, 30, 40, 50]
total =0;
for num in numbers:
    total += num
    print(total)

# Task 7 — if + loop
numbers = [10, 25, 5, 40, 15, 30]
for num in numbers:
    if num>20:
        print(num)

# Task 8 — while
i=1
while i<=5:
    print(i)
    i+=1

# Task 9 — break
for i in range(1,11):
    if i==5:
        break
    print(i)

# Task 10 — continue
for i in range(1,11):
    if i==5:
        continue
    print(i)
