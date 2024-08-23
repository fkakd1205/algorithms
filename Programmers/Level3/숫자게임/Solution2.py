def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    b_idx = 0

    for a_num in A:
        while b_idx < len(B) and a_num >= B[b_idx]:
            b_idx += 1
        
        if b_idx < len(B) and a_num < B[b_idx]:
            answer += 1
            b_idx += 1

    return answer

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(solution(A, B))
