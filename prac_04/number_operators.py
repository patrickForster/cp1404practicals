AMOUNT_OF_NUMBERS = 5
numbers = []
print("Please enter {} numbers when requested".format(AMOUNT_OF_NUMBERS))
for i in range(0, AMOUNT_OF_NUMBERS, 1):
    numbers.append(int(input("Number: ")))
first = numbers[0]
last = numbers[-1]
smallest = min(numbers)
largest = max(numbers)
average = sum(numbers) / len(numbers)
print("The first number is {}".format(first))
print("The last number is {}".format(last))
print("The smallest number is {}".format(smallest))
print("The largest number is {}".format(largest))
print("The average number is {}".format(average))
