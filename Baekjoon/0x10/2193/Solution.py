N = int(input())
f = [0] * (N+1)

f[1] = 1

for i in range(2, N+1):
    f[i] = f[i-1] + f[i-2]

print(f[N])
