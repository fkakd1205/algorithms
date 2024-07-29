S = input().rstrip()
T = input().rstrip()

word = set()
answer = 0

# 이 단어로 구성된 애들만 문자열을 추가했을 때, T가 만들어질 수 있다
for i in range(1, len(T)+1):
    for j in range(len(T)-i+1):
        a = T[j:j+i]
        word.add(a)
        word.add(a[::-1])

def recur(cur):
    global answer

    if len(cur) == len(T):
        if cur == T:
            answer = 1
        return
    
    new_s1 = cur + 'A'
    new_s2 = cur + 'B'
    if new_s1 in word:
        recur(new_s1)
    if new_s2 in word:
        recur(new_s2[::-1])

recur(S)
print(answer)
