from sys import stdin

MX = 123456 * 2
is_prime = [False, False] + [True] * MX
for i in range(2, MX+1):
    if i * i > (MX+1): break
    if not is_prime[i]: continue

    for j in range(i*i, MX+1, i):
        is_prime[j] = False

while(True):
    num = int(stdin.readline().rstrip())

    if num == 0:
        break
    
    cnt = 0
    for i in range(num+1, (2 * num) + 1):
        if is_prime[i]:
            cnt += 1
    print(cnt)
