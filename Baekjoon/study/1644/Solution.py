N = int(input())

prime = [False, False] + ([True] * (N-1))
number = []
answer = 0

# 에라토스테네스 체
for i in range(2, N+1):
    if i * i > N: break
    if not prime[i]: continue

    for j in range(i * i, N + 1, i):
        prime[j] = False

for i in range(2, N+1):
    if prime[i]:
        number.append(i)

# 투포인터
sum = 0
en = 0
for st in range(len(number)):
    while en < len(number) and sum < N:
        sum += number[en]
        en += 1
    
    if sum == N:
        answer += 1

    sum -= number[st]

print(answer)
