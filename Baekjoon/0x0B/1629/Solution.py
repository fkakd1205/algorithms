from sys import stdin

A, B, C = map(int, (stdin.readline().split()))

def new_pow(a, b, c):
    if (b == 1):
        return a % c
    
    X = new_pow(a, b // 2, c)

    # B번의 연산을 다 수행하지 않는다
    # 
    # ex.
    # 10을 11번 곱하지 않고,
    # 10^11을 ((10^5)^2)*10으로 변경
    # 10^5는 (10^2)^2*10으로 변경해 계산
    if (b % 2) :    # 홀수인 경우
        return ((X * X) * a) % c
    else:   # 짝수인 경우
        return (X * X) % c
    
print(new_pow(A, B, C))
