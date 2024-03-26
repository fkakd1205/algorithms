# 1. B의 제곱근 보다 작은 소수들을 고른다.
# 2. 그 수들의 N제곱이 A <= N제곱 <= B 에 부합하는지 확인
A, B = map(int, input().split())
MX = int(B ** 0.5)
is_prime = [False, False] + [True] * (MX-1)

for i in range(2, MX+1):
    if i * i > MX: break
    if not is_prime[i]: continue

    for j in range(i*i, MX+1, i):
        is_prime[j] = False

cnt = 0
for i in range(2, MX+1):
    if not is_prime[i]: continue

    j = i * i
    while(j <= B):
        if j < A:
            j *= i
            continue
        cnt += 1
        j *= i
        
print(cnt)
