from sys import stdin

INF = int(2e9)
N, M = map(int, input().split())
A = [int(stdin.readline().rstrip()) for _ in range(N)]
A.sort()

en = 1
mn = INF

# 투포인터
for st in range(N):
    while (en < N and A[en] - A[st] < M):
        en += 1
    if en == N: break   # 더이상 st 와의 차이가 M 이상일 수 없는 경우 break
    mn = min(mn, A[en] - A[st])

print(mn)
