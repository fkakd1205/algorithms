from sys import stdin

N, C = map(int, input().split())
M = int(input())
infos = [list(map(int, stdin.readline().split())) for _ in range(M)]
# 도착지가 빠른순으로 정렬. 도착지가 빠른순으로 상자를 담아야 함
infos.sort(key= lambda x : x[1])

capa = [C] * N  # 각 마을별로 담을 수 있는 상자 무게 저장
result = 0
for st, en, w in infos:
    loadable_w = C
    # 빠른 도착지 순으로 담을 수 있는 최대 상자를 담는다 (이미 실려있는 상자가 있으면 그 무게를 뺀 만큼)
    for i in range(st, en):
        if loadable_w > min(capa[i], w):
            loadable_w = min(capa[i], w)
    # 담은 상자만큼 빼준다
    for i in range(st, en):
        capa[i] -= loadable_w
    result += loadable_w

print(result)
