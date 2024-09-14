sounds = input()
store = dict({'q' : 0, 'u' : 1, 'a' : 2, 'c' : 3, 'k' : 4})
duck = [[] for _ in range(500)]
answer = 0

for s in sounds:
    if answer == -1: break
    for i in range(len(duck)):
        cur = store[s]
        if not duck[i]:
            if cur == 0:
                duck[i].append(cur)
            else:
                answer = -1
            break
        elif duck[i][-1] + 1 == cur:
            duck[i].append(cur)
            break
        elif duck[i][-1] == 4 and cur == 0:
            duck[i].append(cur)
            break

if answer != -1:
    for i in range(len(duck)):
        if duck[i]:
            if duck[i][-1] == 4:
                answer += 1
            else:
                answer = -1
                break

print(answer)
