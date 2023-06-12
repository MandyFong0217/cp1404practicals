#  write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
# The program should then print asterisks as long as the word.
# Example: if the user enters Pythonista (10 characters), the program should print **********.

mini_length_password = 6
password = input("Input password:")

while len(password) < mini_length_password:
    print("wrong")
    password = input("Input password:")

for i in range(len(password)):
    print("*", end = '')

