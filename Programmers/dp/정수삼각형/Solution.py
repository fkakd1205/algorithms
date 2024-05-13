from copy import deepcopy

def solution(triangle):
    answer = 0
    triangle2 = deepcopy(triangle)

    for x in range(1, len(triangle)):
        for y in range(len(triangle[x])):
            if y == 0:
                triangle2[x][y] = max(triangle2[x][y], triangle[x][y] + triangle2[x-1][y])
            elif y == len(triangle[x]) - 1:
                triangle2[x][y] = max(triangle2[x][y], triangle[x][y] + triangle2[x-1][y-1])
            else:
                triangle2[x][y] = max(triangle[x][y] + triangle2[x-1][y-1], triangle[x][y] + triangle2[x-1][y])
    
    answer = max(triangle2[-1])
    return answer

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
print(solution(triangle))