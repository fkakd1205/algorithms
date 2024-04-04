from sys import stdin

S, E, Q = map(str, input().split())
log = dict()

while(True):
    try:
        time, name = stdin.readline().split()
        if time <= S:
            log[name] = 1
            continue
        if E <= time <= Q and (name in log):
            log[name] = 2
    except:
        break

cnt = 0
for name in log: 
    if log[name] == 2: cnt += 1

print(cnt)
