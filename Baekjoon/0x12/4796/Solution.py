from sys import stdin

cnt = 0
while(True):
    L, P, V = map(int, stdin.readline().split())
    cnt += 1

    if(L == 0 and P == 0 and V == 0): break
    a = V // P
    b = V % P
    
    # 남은 기간이 캠핑장을 이용할 수 있는 기간보다 크다면
    if(L < b):
        b = L
    print("Case %d: %d" %(cnt, a * L + b))
