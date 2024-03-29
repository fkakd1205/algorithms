from sys import stdin

MX = 10000
n = int(input())
nums = [int(stdin.readline().rstrip()) for _ in range(n)]
is_prime = [False, False] + [True] * (MX-1)

for i in range(2, MX+1):
    if i * i > MX: break
    if not is_prime[i]: continue

    for j in range(i * i, MX, i):
        is_prime[j] = False

for num in nums:
    result = tuple()
    for i in range(2, (num // 2) + 1):
        if not is_prime[i]: continue
        if is_prime[num - i]:
            result = (i, num-i)
    
    print(*result)
