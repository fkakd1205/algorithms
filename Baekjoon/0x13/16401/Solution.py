from sys import stdin

M, N = map(int, input().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()

def solve(x):
    cur = 0
    for i in range(N):
        cur += arr[i] // x
    
    return cur >= M

st = 0
en = arr[-1]
while(st < en):
    mid = (st + en + 1) // 2

    # M개 이상으로 나누어지지 않을 때
    if mid == 0:
        break

    if(solve(mid)):
        st = mid
    else:
        en = mid - 1
        
print(st)
