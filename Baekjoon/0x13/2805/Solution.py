from sys import stdin

N, M = map(int, input().split())
trees = list(map(int, stdin.readline().split()))
trees.sort()

def solve(x):
    cur = 0
    for i in range(N):
        if (trees[i] > x):
            cur += trees[i] - x
    
    return cur >= M

st = 0
en = max(trees)
while(st < en):
    mid = (st + en + 1) // 2
    if(solve(mid)): st = mid
    else: en = mid - 1

print(st)
