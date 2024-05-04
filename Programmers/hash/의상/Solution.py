def solution(clothes):
    answer = 1
    store = {}

    for name, type in clothes:
        if type in store:
            store[type].append(name)
        else:
            store[type] = [name]

    # A종류 N개, B종류 M개라면 (N+1) * (M+1)개 조합을 선택할 수 있다
    # 해당 종류의 옷을 선택하지 않는 경우도 있으므로 1 더해준다.
    for s in store:
        answer *= (len(store[s]) + 1)
    
    # 모든 옷을 선택하지 않는 경우는 없으므로 -1
    answer -= 1
    return answer

N = int(input())
arr = [input().split() for _ in range(N)]
print(solution(arr))