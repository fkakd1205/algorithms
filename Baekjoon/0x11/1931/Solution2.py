from sys import stdin

N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

# 회의 시작 시간과 끝나는 시간이 동일한 경우를 위해 x[0]도 정렬이 필요함
arr.sort(key = lambda x : (x[1], x[0]))
end_time = arr[0][1]
count = 1

for i in range(1, N):
    if (end_time <= arr[i][0]):
        end_time = arr[i][1]
        count += 1

print(count)
