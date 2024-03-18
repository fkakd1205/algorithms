from sys import stdin

N = int(input())
score = [int(stdin.readline().rstrip()) for _ in range(N)]
count = 0

prev = score[-1]
for i in range(len(score)-2, -1, -1):
    if (prev <= score[i]):
        sub = score[i] - prev + 1
        score[i] -= sub
        count += sub
    prev = score[i]

print(count)
