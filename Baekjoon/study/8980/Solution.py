from sys import stdin

N, C = map(int, input().split())
M = int(input())
truck = [list(map(int, stdin.readline().split())) for _ in range(M)]
capacity = [0] * (N+1)
total_box = 0

# 빨리 내릴 수 있는 것부터 확인
truck.sort(key= lambda x : x[1])

for i in range(M):
    st, en, w = truck[i]
    loadable = w

    # 담을 수 있는 최대 박스
    for j in range(st, en):
        loadable = min(loadable, C - capacity[j])
    
    for j in range(st, en):
        capacity[j] += loadable

    total_box += loadable

print(total_box)