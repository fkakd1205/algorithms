# V1. 시간초과
# def solution(n, left, right):
#     answer = []
#     arr = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if j <= i:
#                 arr[i][j] = i + 1
#             else:
#                 arr[i][j] = j + 1
   
#     for idx in range(left, right+1):
#         x = idx // n
#         y = idx % n
#         answer.append(arr[x][y])
#     return answer

# V2.
def solution(n, left, right):
    answer = []
    
    for idx in range(left, right + 1):
        x = idx // n
        y = idx % n
        if x == 0: answer.append(y + 1)
        elif y <= x:
            answer.append(x+1)
        else:
            answer.append(y+1)

    return answer

n = int(input())
left = int(input())
right = int(input())
print(solution(n, left, right))
