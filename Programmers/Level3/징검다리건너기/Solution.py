def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        # 연속적으로 징검다리 확인
        for stone in stones:
            # 징검다리를 못 건너는 경우
            if cnt >= k: break
            if stone <= mid:
                cnt += 1
            else:
                cnt = 0

        if cnt < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

    return answer

stones = list(map(int, input().split()))
k = int(input())
print(solution(stones, k))