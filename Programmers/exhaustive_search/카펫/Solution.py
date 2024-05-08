def check(y, w, h):
    if ((w-2) * (h-2) == y):
        return True
    return False

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    # total 개수에 대해 나올 수 있는 w, h을 돌면서 yellow 개수를 확인
    for h in range(1, total+1):
        if total % h != 0: continue
        w = total // h
        if (w >= h and check(yellow, w, h)):
            answer = [w, h]
            break
        
    return answer

brown = int(input())
yellow = int(input())
print(solution(brown, yellow))
