from sys import stdin

LOTTO_NUMBER_COUNT = 6

S = []
arr = []
k = 0

def func(cur):
    global S, arr, k
    
    if cur == LOTTO_NUMBER_COUNT:
        result = []
        for i in range(LOTTO_NUMBER_COUNT):
            result.append(S[arr[i]])
        print(*result)
        return
    
    # 이전의 index를 참고해 선택되지 않은 index부터 탐색
    start_idx = 0 if cur == 0 else arr[cur - 1] + 1
    for i in range(start_idx, len(S)):
        arr[cur] = i
        func(cur + 1)

while(True):
    t_case = list(map(int, stdin.readline().split()))
    k = t_case[0]
    S = t_case[1:k+1]

    if k == 0: break

    arr = [0] * LOTTO_NUMBER_COUNT

    func(0)
    print()
