from sys import stdin

K, N = map(int, input().split())
line = [int(stdin.readline().rstrip()) for _ in range(K)]
line.sort()

# N개 이상으로 나누어지는지 확인
def solve(x):
    cur = 0
    for i in range(K):
        cur += line[i] // x
    
    return cur >= N

st = 1
en = line[-1]
while(st < en):
    mid = (st + en + 1) // 2    # (st == en, st > target)인 경우를 위해 1을 더해준다
    if(solve(mid)): st = mid
    else: en = mid - 1

print(st)
