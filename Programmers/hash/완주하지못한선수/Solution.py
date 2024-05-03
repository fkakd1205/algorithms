def solution(participant, completion):
    record = {}
    answer = ''

    for p in participant:
        if p in record:
            record[p] += 1
        else:
            record[p] = 1

    for c in completion:
        record[c] -= 1

    for name in record:
        if record[name] != 0:
            answer = name
            break

    return answer

p = input().split()
c = input().split()
print(solution(p, c))