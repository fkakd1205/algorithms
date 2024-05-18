def solution(n, results):
    answer = 0
    arr = [[0] * (n+1) for _ in range(n+1)]
    # p1이 p2를 이긴 경우 1로 세팅
    for p1, p2 in results:
        arr[p1][p2] = 1
        arr[p2][p1] = -1

    # 플로이드 알고리즘
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if arr[i][j] != 0: continue
                # i가 k를 이기고, k가 j를 이긴 경우 => i가 j를 이김
                # i가 k에게 지고, k가 j에게 진 경우 => i가 j에게 짐
                if arr[i][k] == arr[k][j]:
                    arr[i][j] = arr[i][k]
                    arr[j][i] = -arr[i][k]
    
    # 0의 개수가 1개인 경우
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if arr[i][j] == 0:
                cnt += 1
        if cnt == 1:
            answer += 1

    return answer

n = int(input())
k = int(input())
results = [list(map(int, input().split())) for _ in range(k)]
print(solution(n, results))
