INF = int(1e9)

N = int(input())
f = [0] * (N+1)

# V1. 
# def recur(n, cnt):
#     if (n == 2 or n == 3):
#         return cnt + 1
    
#     if (f[n] != 0):
#         return cnt + f[n]
    
#     res = INF

#     if (n % 3 == 0):
#         res = min(res, recur(n // 3, cnt + 1))
#     if (n % 2 == 0):
#         res = min(res, recur(n // 2, cnt + 1))
    
#     res = min(res, recur(n - 1, cnt + 1))
#     return res

# for i in range(2, N+1):
#     f[i] = recur(i, 0)

# print(f[N])

# V2.
for n in range(2, N+1):
    res = f[n-1] + 1

    if(n % 3 == 0):
        res = min(res, f[n // 3] + 1)
    if(n % 2 == 0):
        res = min(res, f[n // 2] + 1)
    
    f[n] = res

print(f[n])
