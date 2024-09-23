from sys import stdin
from collections import deque

N = int(input())
friends = [[] for _ in range(N+1)]
result = []

while True:
    a, b = map(int, stdin.readline().split())
    
    if (a, b) == (-1, -1):
        break
    
    friends[a].append(b)
    friends[b].append(a)

def bfs(st):
    q = deque()
    q.append(st)
    check[st] = 0

    while q:
        cur = q.popleft()

        for friend in friends[cur]:
            if check[friend] != -1: continue
            check[friend] = check[cur] + 1
            q.append(friend)

for i in range(1, N+1):
    check = [-1] * (N+1)
    bfs(i)
    result.append(max(check))

score = min(result)
print(score, result.count(score))

for i in range(N):
    if result[i] == score:
        print(i+1, end=' ')
