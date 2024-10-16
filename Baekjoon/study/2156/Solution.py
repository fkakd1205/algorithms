from sys import stdin

n = int(input())
wine = [0] + [int(stdin.readline().rstrip()) for _ in range(n)]
drink = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
    drink[i][0] = max(drink[i-1][0], drink[i-1][2], drink[i-1][1])
    drink[i][1] = drink[i-1][0] + wine[i]
    drink[i][2] = drink[i-1][1] + wine[i]

print(max(drink[n]))
