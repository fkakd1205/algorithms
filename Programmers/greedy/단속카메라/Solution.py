def solution(routes):
    answer = 0
    end_point = -30001
    routes.sort(key = lambda x : x[1])  # 종료지점 기준으로 오름차순

    for route in routes:
        st, en = route
        if end_point < st:
            end_point = en
            answer += 1

    return answer

n = int(input())
routes = [list(map(int, input().split())) for _ in range(n)]
print(solution(routes))
