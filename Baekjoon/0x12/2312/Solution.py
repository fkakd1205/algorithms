from sys import stdin

MX = 100000
T = int(input())
is_prime = [False, False] + [True] * MX

for i in range(2, MX+1):
    if i * i > MX: break
    if not is_prime[i]: continue

    for j in range(i * i, MX, i):
        is_prime[j] = False

for _ in range(T):
    N = int(stdin.readline().rstrip())
    count = [0] * (N+1)

    temp = N
    for i in range(2, N+1):
        if not is_prime[i]:continue
        while(temp % i == 0):
            temp //= i
            count[i] += 1

    for i in range(N+1):
        if count[i] > 0:
            print(i, count[i])
