# 풀이1
# from itertools import combinations

# N, M = map(int, input().split())
# arr = [i for i in range(1, N+1)]

# comb = combinations(arr, M)

# for num in comb:
#     result = []
#     for i in num:
#         result.append(i)
    
#     print(*result)

# 풀이2
N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
isused = [0] * (N+1)

def func(cur):
    if(cur == M):
        result = []
        for i in range(M):
            result.append(arr[i])
        print(*result)
    else:
        # cur != 0 인 경우, 이전 track idx를 참고해서 현재 track idx를 초기화
        track_idx = 1 if cur == 0 else arr[cur-1] + 1
        for i in range(track_idx, N+1):
            if not isused[i]:
                arr[cur] = i
                isused[i] = 1
                func(cur+1)
                isused[i] = 0

func(0)
