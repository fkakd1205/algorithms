A, B, C = map(int, input().split())

def mul(a, b):
    if b == 1:
        return a % C
    temp = mul(a, b // 2)
    if b % 2 == 1:
        return temp * temp * a % C
    else:
        return temp * temp % C

print(mul(A, B))
