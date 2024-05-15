def solution(m, n, puddles):
    answer = 0
    arr = [[0] * (m+1) for _ in range(n+1)]
    arr[1][1] = 1

    # 각 좌표를 지나치는 경로의 수를 arr에 저장
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1: continue
            if [j, i] in puddles: continue
             # 현재 좌표를 지나치는 경로의 수 = 위 좌표를 통해 오는 경우 + 왼쪽 좌표를 통해 오는 경우
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

    answer = arr[n][m] % 1_000_000_007
    return answer

m = int(input())
n = int(input())
k = int(input())
puddles = [list(map(int, input().split())) for _ in range(k)]
print(solution(m, n, puddles))
