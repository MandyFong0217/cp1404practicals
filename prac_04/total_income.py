"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    # 4. Refactor the months variable to a better name.
    number_of_moths = int(input("How many months? "))

    for month in range(1, number_of_moths + 1):
        # 3. Change to f-string
        income = float(input(f"Enter income for month {str(month)} : "))
        incomes.append(income)

    print_report(incomes, number_of_moths)


def print_report(incomes, number_0f_moths):
    """This function will print Income report"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_0f_moths + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
