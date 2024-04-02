from sys import stdin

N, M = map(int, input().split())
d_by_num = dict()
d_by_name = dict()

for i in range(1, N+1):
    name = stdin.readline().rstrip()
    d_by_num[i] = name
    d_by_name[name] = i

for i in range(M):
    search = stdin.readline().rstrip()
    if search.isdigit():
        print(d_by_num[int(search)])
    else:
        print(d_by_name[search])
