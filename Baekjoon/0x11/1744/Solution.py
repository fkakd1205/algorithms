from sys import stdin

N = int(input())
minus = []
plus = []

sum = 0
for _ in range(N):
    num = int(stdin.readline().rstrip())

    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        sum += num   # 1인 경우, 더해주는게 값이 커진다

plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if (len(plus)-1 == i):
        sum += plus[i]
    else:
        sum += (plus[i] * plus[i+1])

for i in range(0, len(minus), 2):
    if (len(minus)-1 == i):
        sum += minus[i]
    else:
        sum += (minus[i] * minus[i+1])

print(sum)
