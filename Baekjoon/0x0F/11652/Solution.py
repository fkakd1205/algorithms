from sys import stdin

N = int(input())

# 풀이1
# num = [int(stdin.readline().rstrip()) for _ in range(N)]
# num.sort()

# max_num = num[0]
# max_cnt = 0
# current_cnt = 1

# for i in range(1, N):
#     if num[i] == num[i-1]: current_cnt += 1
#     else:
#         if(max_cnt < current_cnt):
#             max_cnt = current_cnt
#             max_num = num[i-1]
#         current_cnt = 1

# # 마지막 숫자가 가장 많다면
# if(max_cnt < current_cnt):
#     max_num = num[N-1]

# print(max_num)

# 풀이2
d = dict()
for _ in range(N):
    num = int(stdin.readline().rstrip())

    if num in d:
        d[num] += 1
    else:
        d[num] = 1

result = sorted(d.items(), key = lambda x : (-x[1], x[0]))
print(result[0][0])
