from copy import deepcopy

# 한 칸에서 4번 이상 회전시키는 것은 의미 없다.
# 4 ^ (8 * 8) => 모든 경우 완전탐색 불가능

# 첫째줄을 12시로 맞추면, 둘째줄 돌리면 X
# 따라서 n-1번째 줄을 통해 n번째 줄의 회전 횟수를 결정
# 첫째줄만 돌려서 완탐 + 나머지 줄은 그 윗줄의 회전횟수를 통해 회전 => 최종 마지막 줄이 0으로만 이루어지면 완성
# (4 ^ 8) * (N-1 * N)

# 결국 위의 방향은 변경해 줄 필요 X
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

INF = int(1e9)
dx = [1, 0, 0]
dy = [0, 1, -1]

def rotate(clockHands, x, y, cnt):
    clockHands[x][y] = (clockHands[x][y] + cnt) % 4

    for i in range(3):
        cx = x + dx[i]
        cy = y + dy[i]
        if 0 <= cx < len(clockHands) and 0 <= cy < len(clockHands):
            clockHands[cx][cy] = (clockHands[cx][cy] + cnt) % 4

def solution(clockHands):
    answer = INF
    N = len(clockHands)
    origin = clockHands
    
    # 첫번째 줄 회전 모두 확인
    for k in range(4 ** N):
        clockHands = deepcopy(origin)
        case = k
        total_cnt = 0
        for c in range(N):
            cnt = case % 4
            total_cnt += cnt
            rotate(clockHands, 0, c, cnt)
            case //= 4

        # 2번째 줄부터 윗줄을 참고해 회전 횟수 확인
        for i in range(1, N):
            for j in range(N):
                prev_row = clockHands[i-1][j]
                cnt = (4 - prev_row) % 4
                if cnt == 0:
                    continue
                total_cnt += cnt
                rotate(clockHands, i, j, cnt)

        # N번째 줄이 모두 0인 경우
        if sum(clockHands[-1]) == 0:
            answer = min(answer, total_cnt)

    return answer

N = int(input())
clockHands = [list(map(int, input().split())) for _ in range(N)]
print(solution(clockHands))
