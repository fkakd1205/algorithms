from sys import stdin

N = int(input())

dic = {}

for _ in range(N):
    num = int(stdin.readline().rstrip())
    if num in dic:
        dic[num] = dic[num] + 1
    else:
        dic[num] = 1

sorted_num = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
print(sorted_num[0][0])
