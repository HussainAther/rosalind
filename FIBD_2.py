n = 7
m = 3

k = [1]
for i in range(0, m-1):
    k.append(0)

for i in range(0, n-1):
    k = [sum(k[1:])] + k[:-1]
    print k

print sum(k)