M, N = map(int, input().split())

prime = [False, False] + ([True] * 1000000)

# 에라토스테네스의 체
# 합성수 N에서 1을 제외한 가장 작은 약수는 N의 제곱근 이하이다.
for i in range(2, len(prime)):
    if i * i > len(prime): break
    if not prime[i]: continue

    # i*2 가 아닌 i*i 부터 합성수 처리
    # 5의 배수 10, 15, 20, 25에서 10, 15, 20은 이미 i가 2, 3일 때 False 처리된다
    for j in range(i*i, len(prime), i):
        prime[j] = False

for i in range (M, N+1):
    if prime[i]:
        print(i)
