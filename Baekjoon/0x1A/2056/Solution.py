from sys import stdin

N = int(input())
memo = [0] * (N+1)

for i in range(1, N+1):
    tasks = list(map(int, stdin.readline().split()))
    
    mx = 0
    for j in range(tasks[1]):
        mx = max(mx, memo[tasks[2+j]])
    memo[i] = mx + tasks[0]

print(max(memo))
