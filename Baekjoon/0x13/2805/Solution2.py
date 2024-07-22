from sys import stdin

N, M = map(int, input().split())
height = list(map(int, stdin.readline().split()))

left = 0
right = max(height)
answer = 0

def is_solved(target):
    tree = 0
    for h in height:
        if tree >= M: break
        if h - target > 0: 
            tree += h - target

    return tree >= M

while left <= right:
    mid = (left + right) // 2
    
    if is_solved(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1

print(answer)
