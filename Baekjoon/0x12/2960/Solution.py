N, K = map(int, input().split())
is_prime = [False, False] + [True] * (N-1)
cnt = 0
result = 0

for i in range(2, N+1):
    if not is_prime[i]: continue
    
    flag = False
    for j in range(i, N+1, i):
        if not is_prime[j]: continue
        is_prime[j] = False
        cnt += 1
        if cnt == K:
            flag = True
            result = j
            break
    if flag:
        break

print(result)
