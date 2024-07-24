from sys import stdin
from math import sqrt

N, M = map(int, input().split())
arr = [list(stdin.readline().rstrip()) for _ in range(N)]
mx = -1

for x in range(N):
    for y in range(M):
        for dx in range(-N, N):     # 행 등차 (-N+1이 아닌 -N부터 시작하는 것은 N과 M이 1 1 인 경우를 위함)
            for dy in range(-M, M):     # 열 등차
                if dx == 0 and dy == 0: continue    # dx와 dy가 0이면 서로 같은 칸을 가리킨다
                num = ''
                cx, cy = x, y
                while 0 <= cx < N and 0 <= cy < M:
                    num += arr[cx][cy]
                    # 완전 제곱수 확인
                    if int(sqrt(int(num))) ** 2 == int(num):
                        mx = max(mx, int(num))
                    cx += dx
                    cy += dy

print(mx)
