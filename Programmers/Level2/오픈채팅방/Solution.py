def solution(record):
    answer = []
    users = dict()
    for rec in record:
        log = rec.split()
        if log[0] == "Enter":
            users[log[1]] = log[2]
        elif log[0] == "Change":
            users[log[1]] = log[2]   
    
    for rec in record:
        log = rec.split()
        if log[0] == "Enter":
            answer.append(f"{users[log[1]]}님이 들어왔습니다.")
        elif log[0] == "Leave":
            answer.append(f"{users[log[1]]}님이 나갔습니다.")
    return answer

n = int(input())
record = list(input() for _ in range(n))
print(solution(record))
