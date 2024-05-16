def solution(tickets):
    answer = []
    is_used = [False] * len(tickets)    # 티켓 번호 부여 및 사용 여부 표시

    def dfs(airport, routes):
        if (len(routes) == len(tickets) + 1):
            # 가능한 경로를 모두 추가
            answer.append(routes)
            return
        
        for idx, ticket in enumerate(tickets):
            st, en = ticket
            # 현재 있는 공항에서 갈 수 있는 공항을 추가
            if st == airport and not is_used[idx]:
                is_used[idx] = True
                dfs(en, routes + [en])
                is_used[idx] = False

    dfs("ICN", ["ICN"])
    answer.sort()
    return answer[0]

N = int(input())
tickets = [list(input().split()) for _ in range(N)]
print(solution(tickets))
