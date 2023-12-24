from sys import stdin

N = int(input())

for _ in range(N):
    cloth = dict()
    M = int(stdin.readline().rstrip())
    result = 1
    
    for _ in range(M):
        name, type = list(stdin.readline().split())

        if type in cloth:
            cloth[type] += 1
        else:
            cloth[type] = 1

    # 단독으로도 입을 수 있으므로 +1 
    for idx in cloth:
        result *= (cloth[idx] + 1)

    # 아무것도 안 입는 경우 -1
    print(result-1)
