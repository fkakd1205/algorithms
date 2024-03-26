N = int(input())

a = N // 5
result = -1

for i in range(a, -1, -1):
    temp = N - (i * 5)
    b = temp // 3
    if temp % 3 == 0:
        result = i + b
        break

print(result)
