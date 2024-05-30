from copy import deepcopy

def solution(land):
    answer = 0
    land2 = deepcopy(land)
    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                # 현재 열과 연속되지 않는 열의 값을 더해 비교
                if j == k: continue
                land2[i][j] = max(land2[i][j], land[i][j] + land2[i-1][k])

    answer = max(land2[-1])
    return answer

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]
print(solution(land))
