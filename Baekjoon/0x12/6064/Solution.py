from sys import stdin

T = int(input())

# 최대공약수
def gcd(a, b):
    while(b != 0):
        k = a % b
        a = b
        b = k
    return a

for _ in range(T):
    M, N, x, y = map(int, stdin.readline().split())
    result = -1
    mx = (N // gcd(M, N)) + 1
    
    # (M * k) + x = (N * k') + y 인 조건을 찾는다
    for i in range((mx)):
        a = (M * i) + x
        if ((a-y) % N == 0):
            result = a
            break

    print(result)
