n = int(input())
temp = [0] * (n + 1)

temp[0] = 1
temp[1] = 1

# 1. i-1번째까지 구한 직사각형에 (1*2) 직사각형을 붙인 경우
# 2. i-2번째까지 구한 직사각형에 (2*1) 직사각형 2개를 붙인 경우
# 3. i-2번째까지 구한 직사각형에 (2*2) 직사각형을 붙인 경우
for i in range(2, n+1):
    temp[i] = temp[i-1] + (2 * temp[i-2])

print(temp[n] % 10007)
