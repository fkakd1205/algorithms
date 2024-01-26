N = int(input())
isused1 = [0] * N   # y축
isused2 = [0] * (N * 2 - 1) # 상승 대각선
isused3 = [0] * (N * 2 - 1) # 하강 대각선
count = 0

def func(cur):
    if cur == N:
        global count
        count += 1
    else:
        for i in range(N):
            # 이미 y축, 상승 대각선, 하강 대각선에 퀸이 존재하는 경우
            if (isused1[i] or isused2[i + cur] or isused3[i - cur + N - 1]):
                continue
            isused1[i] = 1
            isused2[i + cur] = 1
            isused3[i - cur + N - 1] = 1
            func(cur + 1)
            isused1[i] = 0
            isused2[i + cur] = 0
            isused3[i - cur + N - 1] = 0

func(0)
print(count)
