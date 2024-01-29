from sys import stdin

N, K = map(int, input().split())
arr = []
result = 0

for _ in range(N):
    arr.append(int(stdin.readline().rstrip()))

arr.sort(reverse=True)

for c in arr:
    a = K // c
    # 현재 돈으로 K원을 채울 수 있다면
    if (a):
        result += a
        K -= (a * c)

print(result)
