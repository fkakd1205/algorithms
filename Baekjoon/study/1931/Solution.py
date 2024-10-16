from sys import stdin

N = int(input())
meeting = [list(map(int, stdin.readline().split())) for _ in range(N)]
meeting.sort(key= lambda x:(x[1], x[0])) # 주의. 회의 시작과 끝나는 시간이 동일할 경우를 위해 x[0]정렬도 필요

cnt = 0
prev = -1

for i in range(N):
    if prev <= meeting[i][0]:
        prev = meeting[i][1]
        cnt += 1

print(cnt)
