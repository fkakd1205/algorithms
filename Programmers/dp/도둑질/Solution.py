def solution(money):
    answer = 0
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)

    # 첫번째 집을 털고, 마지막 집을 털지 못하는 경우 포함
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    # 마지막 집을 털고, 첫번째 집을 털지 못하는 경우 포함
    dp2[1] = money[1]
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    answer = max(dp1[-2], dp2[-1])
    return answer

money = list(map(int, input().split()))
print(solution(money))