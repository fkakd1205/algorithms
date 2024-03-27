from sys import stdin

MX = 1000000
N = int(input())
num = [int(stdin.readline().rstrip()) for _ in range(N)]
is_prime = [False, False] + [True] * (MX)

for i in range(2, MX+1):
    if i * i > MX : break
    if not is_prime[i] : continue

    for j in range(i * i, MX+1, i):
        is_prime[j] = False

for i in range(N):
    cnt = 0
    # num[i] // 2 까지만 확인
    for j in range(2, num[i] // 2 + 1):
        if is_prime[j] and is_prime[num[i] - j]:
            cnt += 1
    
    print(cnt)
