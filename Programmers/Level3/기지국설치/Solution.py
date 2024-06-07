import math

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
#     - o -          -  o - 
def solution(n, stations, w):
    answer = 0
    active_range = 2 * w + 1
    start = 1
    for s in stations:
        end = s - w - start
        # 전파 범위를 이용해 기지국 설치 수를 구한다
        if end > 0:
            answer += math.ceil(end / active_range)
        start = s + w + 1
    
    # 오른쪽에 남은 아파트들
    rest = n - start + 1
    if rest > 0:
        answer += math.ceil(rest / active_range)
    return answer

n = int(input())
stations = list(map(int, input().split()))
w = int(input())
print(solution(n, stations, w))
