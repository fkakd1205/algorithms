from sys import stdin

arr = [list(map(int, stdin.readline().split())) for _ in range(19)]

def check_dir(x, y, dx, dy):
    cnt = 0
    # (x-dx, y-dy)는 이미 검사를 진행했던 칸인데, 현재 색상과 동일하다면 오목이 안된다는 것을 알 수 있음
    if 0 <= x - dx < 19 and 0 <= y - dy < 19 and arr[x][y] == arr[x-dx][y-dy]:
        return False
    # 각 방향별로 6개를 확인한다.
    for i in range(6):
        cx = x + (dx * i)
        cy = y + (dy * i)
        if 0 <= cx < 19 and 0 <= cy < 19:
            if arr[cx][cy] == arr[x][y]:
                cnt += 1
            else:
                break
        else:
            break
    return cnt == 5

# y와 x의 방향을 생각하면 다음 방향들만 확인해주면 된다
# (x, y+1), (x+1, y+1), (x+1, y), (x-1, y+1)
def has_omok(x, y):
    for dx, dy in ((0, 1), (1, 1), (1, 0), (-1, 1)):
        if check_dir(x, y, dx, dy):
            return True
    return False

# y가 작으면서, x가 작은 값의 오목을 먼저 확인한다.
# (0, 0) -> (1, 0) -> (2, 0) -> ... -> (18, 17), (18, 18) 순으로 확인한다
answer = -1, -1
for j in range(19):
    for i in range(19):
        if arr[i][j] != 0:
            if has_omok(i, j):
                answer = i, j
                break
    if answer != (-1, -1): break

if answer == (-1, -1):
    print(0)
else:
    print(arr[answer[0]][answer[1]])
    print(answer[0]+1, answer[1]+1)
