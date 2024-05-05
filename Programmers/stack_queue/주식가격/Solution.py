def solution(prices):
    answer = [0] * (len(prices))
    st = []

    for i in range(len(prices)):
        cur_cost = prices[i]
        
        if not st or st[-1][0] <= cur_cost:
            st.append((cur_cost, i))
        else:
            while (st and st[-1][0] > cur_cost):
                cost, day = st.pop()
                answer[day] = i - day
            st.append((cur_cost, i))
    for cost, day in st:
        answer[day] = (len(prices)-1) - day

    return answer

prices = list(map(int, input().split()))
print(solution(prices))
