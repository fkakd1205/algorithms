N = int(input())

# 별 감소
for i in range(1, N+1):
    print((" " * (i - 1)) + ("*" * (2 * (N - i) + 1)))
# 별 증가
for i in range(1, N):
    print((" " * (N - (i + 1))) + ("*" * ((2 * i) + 1)))
