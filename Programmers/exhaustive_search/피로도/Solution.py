from itertools import permutations

def solution(k, dungeons):
    answer = -1

    for order in permutations(dungeons, len(dungeons)):
        hp = k
        cnt = 0
        for i in range(len(order)):
            if hp < order[i][0]: break
            hp -= order[i][1]
            cnt += 1

        answer = max(answer, cnt)
    return answer

k = int(input())
n = int(input())
dungeons = [list(map(int, input().split())) for _ in range(n)]
print(solution(k, dungeons))
