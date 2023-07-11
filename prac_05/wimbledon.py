"""
Game, Set, Match
Estimate: 30 minutes
Actual:   35 minutes
"""


filename = 'wimbledon.csv'
country = []
champions = []

# read the file and get the list of country and champions
with open(filename, "r", encoding="utf-8-sig") as in_file:
    for i in in_file.readlines():
        line = i.split(',')
        country.append(line[1])
        champions.append(line[2])

champions.remove('Champion')
champions_list = {}
# count the number of the person got champions
for name in champions:
    champions_list[name] = champions_list.get(name, 0) + 1

# print result
print('Wimbledon Champions:')
for name in champions_list:
    print(f'{name} {champions_list[name]}')

print('\n')
country_list = set(country)
country_list.remove('Country')
print(f'These {len(country_list)} countries have won Wimbledon:')
print(','.join(sorted(country_list)))
