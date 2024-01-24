from sys import stdin

N = int(input())
point = [list(map(int, stdin.readline().split())) for _ in range(N)]

# x좌표 기준으로 먼저 정렬 후, y좌표 기준으로 정렬
point.sort(key= lambda x : x[0])
point.sort(key= lambda x : x[1])

for x, y in point:
    print(x, y, sep=" ")
