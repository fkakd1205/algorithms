from sys import stdin

N, C = map(int, input().split())
nums = list(map(int, stdin.readline().split()))
dic = {}

for n in nums:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

sorted_by_freq = sorted(dic.items(), key = lambda x : -x[1])

result = []
for n, freq in sorted_by_freq:
    for _ in range(freq):
        result.append(n)

print(*result)
