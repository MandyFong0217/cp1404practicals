import random

f = open('temps_input.txt', 'w')
number_tem = 3

for i in range(number_tem):
    t = round(random.uniform(-200, 200), 15)
    f.write(str(t))
    f.write('\n')
    print(t)


