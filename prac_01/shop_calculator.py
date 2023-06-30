total_price = 0
num_items = int(input("Number of items:"))
while num_items < 0:
    print("Invalid number of items!")
    num_items = int(input("Number of items:"))

for i in range(num_items):
    price_items = float(input("Price of item::"))
    total_price = total_price + price_items

if total_price > 100:
    total_price = total_price - total_price * 0.1

print('Total price for 3 items is $%.2f'% total_price)

