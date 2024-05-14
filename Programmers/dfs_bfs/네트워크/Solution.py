from collections import deque

computer_cnt = 0
arr = []
check = []

def bfs(st):
    global check
    q = deque()

    for i in range(computer_cnt):
        if arr[st][i] == 1 and not check[i]:
            q.append(i)
            check[i] = True

    while q:
        des = q.popleft()

        for i in range(computer_cnt):
            if arr[des][i] == 1 and not check[i]:
                q.append(i)
                check[i] = True        

def solution(n, computers):
    global computer_cnt, arr, check
    computer_cnt = n
    arr = computers
    check = [False] * n
    answer = 0

    for i in range(n):
        if check[i]: continue
        bfs(i)
        answer += 1

    return answer

n = int(input())
computers = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, computers))
