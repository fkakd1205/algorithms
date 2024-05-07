st_1 = [1, 2, 3, 4, 5]
st_2 = [2, 1, 2, 3, 2, 4, 2, 5]
st_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

def solution(answers):
    answer = []
    scores = [0] * 4

    for i in range(len(answers)):
        ans = answers[i]
        if ans == st_1[i % 5]:
            scores[1] += 1
        if ans == st_2[i % 8]:
            scores[2] += 1
        if ans == st_3[i % 10]:
            scores[3] += 1

    high_score = max(scores)
    for i, score in enumerate(scores):
        if i == 0: continue
        if score == high_score:
            answer.append(i)
    
    return answer

answers = list(map(int, input().split()))
print(solution(answers))
