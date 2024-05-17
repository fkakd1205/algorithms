def solution(n, times):
    answer = 0
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                break
        if cnt >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    return answer

n = int(input())
times = list(map(int, input().split()))
print(solution(n, times))
