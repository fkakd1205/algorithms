from sys import stdin

N = int(input())
meeting = [list(map(int, stdin.readline().split())) for _ in range(N)]
time = 0
cnt = 0

# 회의가 끝나는 동시에 다음 회의가 시작될 수 있는 경우 때문에
# finish_time 정렬 후, start_time 정렬
# ex. (1, 4), (4, 4)가 있다면 (1, 4)가 끝난 후 (4, 4)도 진행할 수 있음
meeting.sort(key= lambda x : (x[1], x[0]))

for start_t, finish_t in meeting:
    # start_t이 이전 회의가 끝난 시간보다 늦은 경우
    if (start_t >= time):
        cnt += 1
        time = finish_t

print(cnt)
