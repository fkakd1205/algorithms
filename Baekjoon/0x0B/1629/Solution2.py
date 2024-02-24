A, B, C = map(int, input().split())

# V1. 시간초과
# def func(x):
#     num = x ** 2
#     return num % C

# result = A
# for i in range(B):
#     result = func(result)

# print(result)

# V2. 나머지 분배 법칙 적용
# (A^B) % C
# A^B = A^(B/2) * A^(B/2) or (A^(B/2)) * (A^(B/2) * A)
# B가 짝수일 때, (A^B) % C = (((A^(B/2)) % C) * ((A^(B/2)) % C)) % C
# B가 홀수일 때, (A^B) % C = (((A^(B/2)) % C) * ((A^(B/2) * A) % C)) % C
def mul(a, b):
    if b == 1:
        return a % C
    else:
        temp = mul(a, b // 2)
        if (b % 2):
            return (temp * temp * a) % C
        else:
            return (temp * temp) % C
        
print(mul(A, B))
