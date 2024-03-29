from sys import stdin

def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp

    return a

n = int(input())
for _ in range(n):
    a, b = map(int, stdin.readline().split())
    x = gcd(a, b)
    a //= x
    b //= x
    print(x * a * b)
