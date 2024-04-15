# V1. 시간초과
# from sys import stdin
# from collections import deque

# n, m = map(int, input().split())
# tree = [[] for _ in range(n+1)]
# arr = list(map(int, stdin.readline().split()))
# q = deque()
# result = [0] * (n+1)

# for i in range(len(arr)):
#     if arr[i] == -1: continue
#     tree[arr[i]].append(i+1)

# def bfs(root, praise):
#     q.append(root)
#     result[root] += praise
    
#     while q:
#         x = q.popleft()

#         for child in tree[x]:
#             result[child] += praise
#             q.append(child)

# for _ in range(m):
#     num, praise = map(int, stdin.readline().split())
#     bfs(num, praise)

# print(*result[1:])

# V2. 해당 번호의 칭찬을 모두 더한 후, 한번의 bfs를 돌아 후배들의 칭찬을 계속해서 더해준다.
from sys import stdin
from collections import deque

n, m = map(int, input().split())
tree = [[] for _ in range(n+1)]
arr = list(map(int, stdin.readline().split()))
q = deque()
result = [0] * (n+1)

for i in range(len(arr)):
    if arr[i] == -1: continue
    tree[arr[i]].append(i+1)

def bfs(cur):
    q.append(cur)
    
    while q:
        x = q.popleft()

        for child in tree[x]:
            result[child] += result[x]
            q.append(child)

for _ in range(m):
    num, praise = map(int, stdin.readline().split())
    result[num] += praise

bfs(1)
print(*result[1:])
