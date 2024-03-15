from sys import stdin

N = int(input())
t = list(map(int, stdin.readline().split()))

t.sort()

for i in range(1, N):
    t[i] += t[i-1]

print(sum(t))
