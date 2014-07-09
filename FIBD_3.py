n = 88
m = 20

pop = [1]
for i in range(0, m-1):
    pop.append(0)

for i in range(0, n-1):
    pop = [sum(pop[1:])] + pop[:-1]
    print pop

print sum(pop)