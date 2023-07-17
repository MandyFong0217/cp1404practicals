"""
stores users' emails by  dictionary
Estimate: 30 minutes
Actual:   10 minutes
"""

account_list = {}
# get the email address
email = input("Email: ")
while email != '':
    name = email.split('@')
    # get the username by finding the word before @
    name = name[0].split('.')
    name = ' '.join(name).title()
    answer = input(f"Is your name {name}?(Y/n)").upper()
    if answer != '' and answer != 'Y':
        name = input("Name: ")
    account_list[name] = email
    email = input("Email: ")

print('\n')
# print all the result
for i in account_list.keys():
    print(f"{i} ({account_list[i]})")
