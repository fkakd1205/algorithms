from sys import stdin
from heapq import heappush, heappop

N = int(input())
min_heap = []
max_heap = []
is_solved = dict()  # {문제번호 : solved 여부}

for i in range(N):
    problem, level = map(int, stdin.readline().split())
    heappush(min_heap, (level, problem))
    heappush(max_heap, (-level, -problem))  # 같은 level이면 가장 큰 문제번호를 찾기 위해 -problem을 넣는다
    is_solved[problem] = False

M = int(input())

for _ in range(M):
    command = stdin.readline().split()

    if(command[0] == 'recommend'):
        if(command[1] == '1'):
            while(max_heap and is_solved[-max_heap[0][1]]):
                heappop(max_heap)
            print(-max_heap[0][1])
        else:
            while(min_heap and is_solved[min_heap[0][1]]):
                heappop(min_heap)
            print(min_heap[0][1])
    elif(command[0] == 'add'):
        p = int(command[1])
        l = int(command[2])
        heappush(min_heap, (l, p))
        heappush(max_heap, (-l, -p))
        # 새로 추가된 문제는 is_solved {문제번호 : False} 로 변경
        is_solved[p] = False
    else:
        is_solved[int(command[1])] = True
        # 푼 문제는 힙에서 제거
        while(min_heap and is_solved[min_heap[0][1]]): heappop(min_heap)
        while(max_heap and is_solved[-max_heap[0][1]]): heappop(max_heap)
