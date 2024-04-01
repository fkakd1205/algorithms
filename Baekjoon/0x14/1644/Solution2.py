N = int(input())
is_prime = [False, False] + [True] * (N-1)

for i in range(2, N+1):
    if i * i > N: break
    if not is_prime[i]: continue

    for j in range(i * i, N+1, i):
        is_prime[j] = False

prime = []
for i in range(N+1):
    if is_prime[i]:
        prime.append(i)

en = 1
sum = 0
if len(prime) > 0:
    sum = prime[0]
cnt = 0
for st in range(len(prime)):
    while (en < len(prime) and sum < N):
        sum += prime[en]
        en += 1
    
    if sum == N: cnt += 1
    elif sum < N: break
    sum -= prime[st]
    

print(cnt)
