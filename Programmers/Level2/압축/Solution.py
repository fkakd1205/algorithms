dic = dict()

for i in range(26):
    dic[chr(ord('A') + i)] = i+1

def solution(msg):
    answer = []
    st, en = 0, 0
    while True:
        if en >= len(msg):
            break

        temp = ''
        # 사전에 이미 존재하는 단어를 temp에 추가
        while en < len(msg) and (msg[st:en+1] in dic):
            temp = msg[st:en+1]
            en += 1
        
        answer.append(dic[temp])
        # 사전에 없는 단어 사전에 추가
        dic[msg[st:en+1]] = len(dic) + 1
        st = en
        
    return answer

msg = input()
print(solution(msg))
