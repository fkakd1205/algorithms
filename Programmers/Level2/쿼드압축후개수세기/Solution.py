arr2 = []
count = [0] * 2

def quadrant(x, y, size):
    num = arr2[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr2[i][j] != num:
                size //= 2
                quadrant(x, y, size)    # 2사분면
                quadrant(x, y + size, size)     # 1사분면
                quadrant(x + size, y, size)     # 3사분면
                quadrant(x + size, y + size, size)      # 4사분면
                return
    count[num] += 1

def solution(arr):
    global arr2
    answer = []
    arr2 = arr
    quadrant(0, 0, len(arr))
    answer = count
    return answer

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
print(solution(arr))
