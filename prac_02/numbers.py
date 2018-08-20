NUMBERS_FILE = "numbers.txt"
in_file = open(NUMBERS_FILE, 'r')
amount = 0
for line in in_file:
    number = int(line)
    amount += number
print(amount)
in_file.close()
