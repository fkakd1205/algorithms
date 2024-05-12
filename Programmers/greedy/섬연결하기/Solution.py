from heapq import heappush, heappop

parent = []

def find_p(x):
    global parent
    if parent[x] != x:
        parent[x] = find_p(parent[x])
    return parent[x]

def union_p(x, y):
    x = find_p(x)
    y = find_p(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def solution(n, costs):
    global parent
    answer = 0
    min_heap = []
    cnt = 0
    parent = [i for i in range(n)]

    for cost in costs:
        heappush(min_heap, (cost[2], cost[0], cost[1]))

    while (cnt + 1 < n):
        c, a, b = heappop(min_heap)
        if find_p(a) != find_p(b):
            union_p(a, b)
            cnt += 1
            answer += c

    return answer

n = int(input())
m = int(input())
costs = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, costs))
