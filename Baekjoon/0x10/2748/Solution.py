n = int(input())

f = [0] * (n+1)

for i in range(1, n+1):
    if i == 1 or i == 2:
        f[i] = 1
        continue
    f[i] = f[i-1] + f[i-2]

print(f[n])
