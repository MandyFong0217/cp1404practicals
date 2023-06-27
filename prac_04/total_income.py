"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_0f_moths = int(input("How many months? "))

    for month in range(1, number_0f_moths + 1):
        income = float(input(f"Enter income for month {str(month)} : "))
        incomes.append(income)

    print_report(incomes, number_0f_moths)


def print_report(incomes, number_0f_moths):
    """This function will print report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_0f_moths + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()