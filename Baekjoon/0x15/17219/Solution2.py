from sys import stdin

N, M = map(int, input().split())
secret = dict()

for _ in range(N):
    site, pw = map(str, stdin.readline().split())
    secret[site] = pw

for _ in range(M):
    search = stdin.readline().rstrip()
    print(secret[search])
