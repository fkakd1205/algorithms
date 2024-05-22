def solution(k, tangerine):
    answer = 0
    store = dict()
    for t in tangerine:
        if t in store:
            store[t] += 1
        else:
            store[t] = 1
    
    sorted_tangerine = sorted(store.items(), key = lambda x: -x[1])
    
    for _, cnt in sorted_tangerine:
        if k <= 0: break
        k -= cnt
        answer += 1
            
    return answer

k = int(input())
tangerine = list(map(int, input().split()))
print(solution(k, tangerine))
