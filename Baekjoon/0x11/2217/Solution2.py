from sys import stdin

N = int(input())
weight = [int(stdin.readline().rstrip()) for _ in range(N)]
weight.sort(reverse=True)

max_w = weight[0]
for i in range(1, N):
    max_w = max(max_w, weight[i] * (i+1))

print(max_w)
