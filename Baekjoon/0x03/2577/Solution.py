A = int(input())
B = int(input())
C = int(input())

num = [0] * 10
mul = str(A * B * C)

for c in mul:
    num[int(c)] += 1

print(*num, sep='\n')
