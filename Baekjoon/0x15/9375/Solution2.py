from sys import stdin

T = int(input())
for _ in range(T):
    n = int(stdin.readline().rstrip())
    cloth = dict()
    result = 1

    for _ in range(n):
        name, kind = map(str, stdin.readline().split())
        
        if kind in cloth:
            cloth[kind] += 1
        else:
            cloth[kind] = 1

    for k in cloth:
        result *= (cloth[k] + 1)

    print(result - 1)   # 아무것도 안입은 경우를 빼준다
