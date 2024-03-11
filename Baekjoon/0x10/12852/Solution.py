N = int(input())
f = [0] * (N+1)
pre = [0] * (N+1)

for i in range(2, N+1):
    res = f[i-1] + 1
    pre[i] = i-1

    if (i % 2 == 0 and res > f[i//2] + 1):
        res = min(res, f[i//2] + 1)
        pre[i] = i//2
    if (i % 3 == 0 and res > f[i//3] + 1):
        res = min(res, f[i//3] + 1)
        pre[i] = i//3
    
    f[i] = res

print(f[N])

result = [N]
cur = N
while(pre[cur] != 0):
    result.append(pre[cur])
    cur = pre[cur]

print(*result)
