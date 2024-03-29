E = 15
S = 28
M = 19
x, y, z = map(int, input().split())

year = 1
while (True):
    if ((year - x) % E == 0 and (year - y) % S == 0 and (year - z) % M == 0):
        break
    year += 1

print(year)
