from sys import stdin

# V1. 시간초과
# n = int(input())
# arr = [([0] * n) for _ in range(n)]

# for i in range(n):
#     num = list(map(int, stdin.readline().split()))

#     for j in range(len(num)):
#         arr[i][j] = num[j]

# mx = 0
# def recur(x, y, sum):
#     global mx
#     if(x == n-1):
#         mx = max(mx, sum)
#         return
    
#     recur(x+1, y, sum + arr[x+1][y])
#     recur(x+1, y+1, sum + arr[x+1][y+1])

# recur(0, 0, arr[0][0])
# print(mx)

# V2.
n = int(input())
arr = [([0] * n) for _ in range(n)]

for i in range(n):
    num = list(map(int, stdin.readline().split()))

    for j in range(len(num)):
        arr[i][j] = num[j]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[n-1]))
