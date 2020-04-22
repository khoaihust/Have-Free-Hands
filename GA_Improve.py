# Chac chan in ra ket qua toi uu
# Khac biet o cho thơi gian nhanh hay lau
# Chay cac test ket qua cao nhat la 42s

import random
import operator

# bieu dien ca the
def init():
    tmp = {}
    tmp['x'] = random.random()*10-5
    tmp['y'] = random.random()*10-5
    tmp['fitness'] = (tmp['x']**2 + tmp['y']-11)**2 + (tmp['x'] + tmp['y']**2 - 7)**2
    return tmp
print('1. Bieu dien ca the:')
print(init())

# khoi tao quan the
population = []
for i in range(10):
    population.append(init())
print('2. Khoi tao quan the:')
print(population[0])

# lai ghep
def crossover(indi1, indi2):
    tmp = {}
    tmp['x'] = random.random()*abs(indi1['x'] - indi2['x']) + min(indi1['x'], indi2['x'])
    tmp['y'] = random.random()*abs(indi1['y'] - indi2['y']) + min(indi1['y'], indi2['y'])
    tmp['fitness'] = (tmp['x']**2 + tmp['y']-11)**2 + (tmp['x'] + tmp['y']**2 - 7)**2
    return tmp
print('3. Lai ghep:')
print(crossover(population[0], population[1]))

# dot bien
def mutation(indi):
    tmp = {}
    tmp['x'] = min(max(indi['x'] + random.random()*2-1, -5), 5)
    tmp['y'] = min(max(indi['y'] + random.random()*2-1, -5), 5)
    tmp['fitness'] = (tmp['x']**2 + tmp['y']-11)**2 + (tmp['x'] + tmp['y']**2 - 7)**2
    return tmp
print('4. Dot bien:')
print(mutation(population[0]))

# lua chon ca the
def selection(popu):
    tmp = sorted(popu, key = lambda k: k['fitness'])
    return tmp[:10]
print('5. Lua chon ca the:')
print(selection(population))

# tien hoa
t = 0
fit =  1
while fit > 0.00001: # loop util fitness value is less than 0.00001
    for i in range(10):
        j = random.randint(0, 9)
        while j == i:
            j = random.randint(0, 9)
        population.append(crossover(population[i], population[j]))
        r = random.random()
        if r < 0.5:
            population.append(mutation(population[i]))
    population.sort(key = lambda k: k['fitness'])
    population = population[:10]
    fit = population[0]['fitness']
    t += 1
    if t > 100:                        # run 100 times, if fitness value is more than 0.00001 
        population.insert(0, init())   # then create individual, insert into first population
        t = 0
print('6. Tien hoa:')
print(population[:10])

# dau ra
print('7. Ket qua:')
print(population[0])
