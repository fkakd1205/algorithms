from sys import stdin

N = int(input())
num = list(map(int, stdin.readline().split()))

is_prime = [False, False] + [True] * 1000

for i in range(2, 1001):
    if(i * i > 1000): break
    if(not is_prime[i]): continue

    for j in range(i * i, 1001, i):
        is_prime[j] = False

result = 0
for i in range(N):
    if(is_prime[num[i]]):
        result += 1

print(result)
