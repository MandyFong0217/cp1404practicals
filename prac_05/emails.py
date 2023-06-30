account_list = {}

email = input("Email: ")
while email != '':
    name = email.split('@')
    name = name[0].split('.')
    name = ' '.join(name).title()
    answer = input(f"Is your name {name}?(Y/n)").upper()
    if answer != '':
        if answer != 'Y':
            name = input("Name: ")
    account_list[name] = email
    email = input("Email: ")

print('\n')
for i in account_list.keys():
    print(f"{i} ({account_list[i]})")
