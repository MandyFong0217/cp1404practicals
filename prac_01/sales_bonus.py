"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

# part a
"""""
sales = float(input("Enter sales: $"))
bonus = 0

if sales >= 1000:
    bonus = 0.15
    print(int(sales * bonus))
else:
    bonus = 0.1
    print(int(sales * bonus))
"""""

# part b
bonus = 0
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = 0.15
        print(int(sales * bonus))
    else:
        bonus = 0.1
        print(int(sales * bonus))
    sales = float(input("Enter sales: $"))
print("Thank you!")