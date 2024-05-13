def solution(N, number):
    answer = -1
    dp = [set()] + [set([int(str(N) * i)]) for i in range(1, 9)]

    # n은 N의 개수. 최대 8까지만 탐색
    for n in range(1, 9):
        # N이 n개 구성된 수 = N이 k개 구성된 수 (+-*/) N이 n-k개 구성된 수
        for k in range(1, n):
            for num1 in dp[k]:
                for num2 in dp[n-k]:
                    dp[n].add(num1 + num2)
                    dp[n].add(num1 - num2)
                    dp[n].add(num1 * num2)
                    if num2 != 0:
                        dp[n].add(num1 // num2)

        if number in dp[n]:
            answer = n
            break

    return answer

N = int(input())
number = int(input())
print(solution(N, number))
