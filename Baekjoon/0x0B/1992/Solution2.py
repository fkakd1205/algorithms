from sys import stdin

N = int(input())
arr = [list(map(int, stdin.readline().rstrip())) for _ in range(N)]

result = ""
def recur(row, col, size):
    global result
    comp = arr[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if (comp != arr[i][j]):
                result += "("
                size //= 2
                recur(row, col, size)   # 왼쪽 위
                recur(row, col + size, size)    # 오른쪽 위
                recur(row + size, col, size)    # 왼쪽 아래
                recur(row + size, col + size, size)     # 오른쪽 아래
                result += ")"
                return

    result += str(comp)

recur(0, 0, N)
print(result)
