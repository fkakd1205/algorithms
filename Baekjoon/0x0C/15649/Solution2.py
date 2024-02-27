N, M = map(int, input().split())

arr = [0] * (N+1)   # M자리 숫자를 저장하는 배열
isused = [False] * (N+1)    # 숫자 사용 여부를 저장하는 배열

def func(cnt):
    if (cnt == M):
        result = []
        for i in range(M):
            result.append(arr[i])
        print(*result)
        return
    else:
        for i in range(1, N+1):
            if not isused[i]:
                arr[cnt] = i
                isused[i] = True
                func(cnt + 1)
                isused[i] = False

func(0)