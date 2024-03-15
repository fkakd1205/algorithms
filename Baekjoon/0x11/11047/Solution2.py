from sys import stdin

N, K = map(int, input().split())
arr = [int(stdin.readline().rstrip()) for _ in range(N)]

money = K
result = 0
for i in range(N-1, -1, -1):
    if (money // arr[i] > 0):
        div = money // arr[i]
        result += div
        money -= arr[i] * div

print(result)
