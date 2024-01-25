from sys import stdin

N, C = map(int, input().split())
num = list(map(int, stdin.readline().split()))

d = dict()
for i in range(N):
    if num[i] in d:
        d[num[i]] += 1
    else:
        d[num[i]] = 1

freq_sorted_num = sorted(d.items(), key = lambda x : (-x[1]))
result = []
for number, freq in freq_sorted_num:
    result += [number] * freq

print(*result)
