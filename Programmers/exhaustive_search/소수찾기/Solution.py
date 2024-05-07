from itertools import permutations

INF = int(1e7)
is_prime = [False, False] + [True] * (INF+1)

# 소수 판별
for i in range(2, INF):
    if i * i > INF: break
    if not is_prime[i]: continue
    is_prime[i] = True

    for j in range(i * i, INF+1, i):
        is_prime[j] = False

def solution(numbers):
    answer = 0
    p = []
    numbers = list(map(str, numbers.rstrip()))
    prime_num = []

    for i in range(1, len(numbers)+1):
        p += list(set(permutations(numbers, i)))     # 순열조합을 구한다
    
    for comp in p:
        num = int(''.join(list(comp)))
        if is_prime[num]:
            prime_num.append(num)

    answer = len(set(prime_num))
    return answer

numbers = input()
print(solution(numbers))
