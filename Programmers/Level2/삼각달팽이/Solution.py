def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n+1)]
    x, y = -1, 0
    num = 1

    # i에 따라 방향이 결정된다
    for i in range(n):
        # i에 방향에 따라 몇개의 데이터를 세팅할지 선택
        for _ in range(i, n):
            # 3방향을 결정할 수 있다
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -=1
                y -=1
            arr[x][y] = num
            num += 1
    
    answer = sum(arr,[])
    return answer

n = int(input())
print(solution(n))
