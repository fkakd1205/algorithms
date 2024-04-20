from sys import stdin

T = int(input())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    routes = [list(map(int, stdin.readline().split())) for _ in range(M)]
    print(N-1)