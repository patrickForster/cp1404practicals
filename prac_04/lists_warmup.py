numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = [3, 1, 4, 1, 5, 9]
# numbers[3:4] = TypeError
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Question 1
numbers[0] = 10
print(numbers)

# Question 2
numbers[-1] = 1
print(numbers)

# Question 3
print(numbers[2:])

# Question 4

for char in numbers:
    if char == 9:
        search = True
        break
    else:
        search = False
print(search)
