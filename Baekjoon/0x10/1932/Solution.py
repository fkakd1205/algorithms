from sys import stdin

n = int(input())
num = [0] * n

for i in range(n):
    num[i] = list(map(int, stdin.readline().split()))

for i in range(1, n):
    for j in range(len(num[i])):
        # j가 첫번째, 마지막일 때는 윗줄에서 더해지는 값이 정해져 있음
        if j == 0 :
            num[i][j] = num[i-1][j] + num[i][j]
        elif j == len(num[i])-1:
            num[i][j] = num[i-1][j-1] + num[i][j]
        else:
            num[i][j] = max(num[i-1][j], num[i-1][j-1]) + num[i][j]

print(max(num[n-1]))
