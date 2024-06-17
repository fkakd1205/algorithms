def solution(sequence, k):
    answer = [-1, -1]
    st = 0
    en = 0
    s = sequence[st]
    while en <= len(sequence):
        # 합이 k와 일치할 때
        if s == k:
            # 조건2. 조건3
            if answer[0] == -1 or (answer[1] - answer[0] > en - st):
                answer[0] = st
                answer[1] = en
            s -= sequence[st]
            st += 1
        elif s > k:
            s -= sequence[st]
            st += 1
            continue
    
        en += 1
        if en < len(sequence):
            s += sequence[en]
    return answer

sequence = list(map(int, input().split()))
k = int(input())
print(solution(sequence, k))
