number_of_items = int(input("Number of Items: "))
total_price = 0.0
while number_of_items <= 0:
    print("Number of items is invalid")
    number_of_items = int(input("Number of Items: "))

for i in range(0, number_of_items, 1):
    item_price = float(input("Cost of Item: $"))
    total_price += item_price

print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
