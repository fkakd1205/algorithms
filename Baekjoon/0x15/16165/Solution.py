from sys import stdin

N, M = map(int, input().split())
dic_by_group = dict()
dic_by_name = dict()

for _ in range(N):
    group_name = stdin.readline().rstrip()
    g_num = int(stdin.readline().rstrip())
    names = [stdin.readline().rstrip() for _ in range(g_num)]
    names.sort()
    dic_by_group[group_name] = names
    for name in names:
        dic_by_name[name] = group_name

for _ in range(M):
    search = stdin.readline().rstrip()
    type = int(stdin.readline().rstrip())
    
    if type == 0:
        print(*dic_by_group[search], sep='\n')
    else:
        print(dic_by_name[search])
