def solution(sequence, k):
    answer = []
    N = len(sequence)
    l, r = 0, N
    
    # 투포인터
    en = 0
    sum = sequence[en]
    for st in range(0, len(sequence)):
        while sum < k and en < N:
            en += 1
            if en == N: break
            sum += sequence[en]

        if sum == k:
            if en - st < r - l:
                l, r = st, en
                answer = [l, r]
        
        sum -= sequence[st]

    return answer

k = int(input())
sequence = list(map(int, input().split()))
print(solution(sequence, k))