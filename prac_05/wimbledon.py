filename = 'wimbledon.csv'
country = []
champions = []


with open(filename, "r", encoding="utf-8-sig") as in_file:
    for i in in_file.readlines():
        line = i.split(',')
        #print(line)
        country.append(line[1])
        champions.append(line[2])

champions.remove('Champion')
champions_list = {}
for name in champions:
    champions_list[name] = champions_list.get(name, 0) + 1

print('Wimbledon Champions:')
for name in champions_list:
    print(f'{name} {champions_list[name]}')

print('\n')
country_list = set(country)
country_list.remove('Country')
print(f'These {len(country_list)} countries have won Wimbledon:')
print(','.join(sorted(country_list)))

