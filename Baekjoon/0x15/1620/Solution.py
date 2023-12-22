from sys import stdin

N, M = map(int, input().split())
dogam_by_name = dict()
dogam_by_order = dict()

for idx in range(1, N+1):
    key = input()
    dogam_by_name[key] = idx
    dogam_by_order[idx] = key

for _ in range(M):
    search = stdin.readline().rstrip()
    
    if search.isdigit():
        print(dogam_by_order[int(search)])
    else:
        print(dogam_by_name[search])
