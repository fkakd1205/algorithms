from sys import stdin

N, M = list(map(int, stdin.readline().split()))
temp = dict()

for _ in range(N):
    url, pwd = list(stdin.readline().split())
    temp[url] = pwd

for _ in range(M):
    search_url = stdin.readline().rstrip()
    print(temp[search_url])
