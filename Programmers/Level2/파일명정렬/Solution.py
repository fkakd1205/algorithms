def sort_head(x):
    # 숫자 전까지, 대소문자 구분하지 않고 사전순
    idx = len(x)
    for i in range(len(x)):
        if x[i].isdigit():
            idx = i
            break
    
    return x[:idx].lower()

def sort_number(x):
    st = 0
    en = len(x)
    for i in range(len(x)):
        if x[i].isdigit() and st == 0:
            st = i
        elif st != 0 and not x[i].isdigit():
            en = i
            break
    return int(x[st:en])

def solution(files):
    answer = sorted(files, key=lambda x : (sort_head(x), sort_number(x)))
    return answer

n = int(input())
files = list(input() for _ in range(n))
print(solution(files))
