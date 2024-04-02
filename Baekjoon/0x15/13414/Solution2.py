from sys import stdin

K, L = map(int, input().split())
wait = dict()

for i in range(1, L+1):
    sid = stdin.readline().rstrip()
    wait[sid] = i

result = sorted(wait.items(), key= lambda x : x[1])

for res in result[:K]:
    print(res[0])
    