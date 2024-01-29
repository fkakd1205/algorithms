from sys import stdin

N = int(input())
time = list(map(int, stdin.readline().split()))

time.sort()

# time[i] = (이전사람의 대기시간 + 소요시간) + i의 소요시간
for i in range(1, N):
    time[i] = time[i-1] + time[i]

print(sum(time))
