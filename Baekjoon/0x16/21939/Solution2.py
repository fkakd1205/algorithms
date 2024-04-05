from sys import stdin
from heapq import heappush, heappop

N = int(input())
min_heap = []
max_heap = []
is_solved = [True] * 100001

for _ in range(N):
    num, level = map(int, stdin.readline().split())

    heappush(min_heap, (level, num))
    heappush(max_heap, (-level, -num))
    is_solved[num] = False

M = int(input())
for _ in range(M):
    command = list(map(str, stdin.readline().split()))

    if command[0] == 'add':
        num = int(command[1])
        level = int(command[2])

        # 난이도, 문제번호 순으로 최소힙 & 최대힙에 넣는다
        heappush(min_heap, (level, num))
        heappush(max_heap, (-level, -num))
        is_solved[num] = False
    elif command[0] == 'recommend':
        if int(command[1]) == 1:
            level, num = max_heap[0]
            print(-num)
        else:
            level, num = min_heap[0]
            print(num)
    else:
        num = int(command[1])
        is_solved[num] = True

    # solved된 문제 동기화
    while (min_heap and is_solved[min_heap[0][1]]):
        heappop(min_heap)
    while (max_heap and is_solved[-max_heap[0][1]]):
        heappop(max_heap)
