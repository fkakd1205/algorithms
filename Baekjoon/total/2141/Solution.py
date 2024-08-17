from sys import stdin

N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
arr.sort()
total = 0
sum = 0

for i in range(N):
    total += arr[i][1]

# 전체 인원 중, 절반이 넘어가는 위치가 답
for i in range(N):
    sum += arr[i][1]
    if sum >= (total / 2):
        print(arr[i][0])
        break
