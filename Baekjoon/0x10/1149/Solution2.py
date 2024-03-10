from sys import stdin

N = int(input())
house = [list(map(int, stdin.readline().split())) for _ in range(N)]

# i번째 집은 i-1번째 집만 확인하면 된다
for i in range(1, N):
    house[i][0] = min(house[i][0] + house[i-1][1], house[i][0] + house[i-1][2])
    house[i][1] = min(house[i][1] + house[i-1][0], house[i][1] + house[i-1][2])
    house[i][2] = min(house[i][2] + house[i-1][0], house[i][2] + house[i-1][1])

print(min(house[N-1][0], house[N-1][1], house[N-1][2]))
