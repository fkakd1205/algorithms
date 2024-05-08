from sys import setrecursionlimit
setrecursionlimit(10**4)

vowel = ['A', 'E', 'I', 'O', 'U']
cnt = 0
search_word = ''
answer = 0

def recur(cur, search):
    global answer, cnt

    if search == search_word:
        answer = cnt
        return
    if cur == 5: return

    # 글자 중복 허용
    for i in range(5):
        cnt += 1
        recur(cur+1, search + vowel[i])

def solution(word):
    global search_word, answer
    search_word = word
    recur(0, '')
    return answer

word = input()
print(solution(word))
