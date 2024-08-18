from sys import stdin

N, C = map(int, input().split())
M = int(input())
infos = [list(map(int, stdin.readline().split())) for _ in range(M)]
capa = [C] * N
answer = 0

# 도착지가 빠른 순으로 정렬
infos.sort(key= lambda x : x[1])

for st, en, box in infos:
    loadable_box = C
    # 현재 범위에서 실을 수 있는 최대 박스 수
    for i in range(st, en):
        if min(capa[i], box) < loadable_box:
            loadable_box = min(capa[i], box)
    
    # capa[index]에는 해당 마을에서 실을 수 있는 박스 수가 갱신
    for i in range(st, en):
        capa[i] -= loadable_box
    answer += loadable_box

print(answer)    
    