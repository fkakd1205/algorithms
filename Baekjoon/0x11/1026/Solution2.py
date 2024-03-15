from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
S = 0

A.sort()
B.sort()

for i in range(N):
    S += A[i] * B[N-1-i]

print(S)
