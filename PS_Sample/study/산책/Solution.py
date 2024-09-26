from sys import stdin

N, T = map(int, input().split())
employee  = [list(map(int, stdin.readline().split())) for _ in range(N)]
group = []

employee.sort(key=lambda x: (-x[0], x[1]))

for st, speed in employee:
    next = st + (speed * T)
    if not group:
        group.append(next)
    elif group[0] > next:
        group.append(next)

print(len(group))
