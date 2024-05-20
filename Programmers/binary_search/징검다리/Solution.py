def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    left = 1
    right = distance

    while left <= right:
        mid = (left + right) // 2
        prev = 0
        rm_cnt = 0
        for rock in rocks:
            # rocks 중 n개를 제거했을 때 최소 거리가 mid가 되려면
            # 이전 rock과의 거리가 mid보다 작다면 돌을 제거
            if rock - prev < mid:
                rm_cnt += 1
                # 이미 n개 제거되었다면
                if rm_cnt > n:
                    break
            else:
                prev = rock
                
        if rm_cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid

    return answer

distance = int(input())
rocks = list(map(int, input().split()))
n = int(input())
print(solution(distance, rocks, n))
