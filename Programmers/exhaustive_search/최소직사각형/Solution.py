def solution(sizes):
    answer = 0
    mx_w = 0
    mx_h = 0

    for w, h in sizes:
        if w < h:
            w, h = h, w

        mx_w = max(w, mx_w)
        mx_h = max(h, mx_h)
    
    answer = mx_w * mx_h
    return answer

N = int(input())
sizes = [list(map(int, input().split())) for _ in range(N)]
print(solution(sizes))
