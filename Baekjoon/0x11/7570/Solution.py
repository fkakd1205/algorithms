from sys import stdin

N = int(input())
child = list(map(int, stdin.readline().split()))

# 현재 서있는 위치를 저장
pos = [0] * (N+1)
for i in range(N):
    pos[child[i]] = i

# 나보다 큰 수가 나보다 뒤에 위치하고 있다면 나와 그 수들은 이동하지 않아도됨
# 위의 조건으로 가장 길게 오름차순을 만족하는 경우를 찾는다
cnt = 0
max_cnt = 0
for i in range(N):
    if pos[i] < pos[i+1]:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 1

result = 0
if N != 1:
    result = N - max_cnt

print(result)
