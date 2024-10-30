from sys import stdin

MAX = 1000_000
prime = [False, False] + [True] * (MAX-1)

for i in range(2, MAX+1):
    if i * i > MAX: break
    if not prime[i]: continue

    for j in range(i*i, MAX+1, i):
        prime[j] = False

while True:
    n = int(stdin.readline().rstrip())
    is_find = False

    if n == 0: break

    # 홀수만 확인
    for i in range(3, (n//2)+1, 2):
        if prime[i] and prime[n-i]:
            print(f"{n} = {i} + {n-i}")
            is_find=True
            break

    if not is_find:
        print("Goldbach's conjecture is wrong")
