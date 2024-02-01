from sys import stdin

N, M = map(int, input().split())
A = []

for _ in range(N):
    A.append(int(stdin.readline().rstrip()))

A.sort()

en = 0
result = int(2e9)
# st, en 을 사용해 이중 for문 검사를 단일 for문 검사로 대체
for st in range(N):
    while(en < N and A[en] - A[st] < M): en += 1
    if(en == N): break
    result = min(result, A[en] - A[st])

print(result)
