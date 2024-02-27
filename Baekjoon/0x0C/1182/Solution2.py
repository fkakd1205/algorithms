from sys import stdin

N, S = map(int, input().split())
arr = list(map(int, stdin.readline().split()))
result = 0

def func(count, sum):
    global result

    if count == N:
        if sum == S:
            result += 1
        return
    
    func(count + 1, sum)
    func(count + 1, sum + arr[count])

func(0, 0)

# 공집합인 경우 -1
if S == 0:
    result -= 1

print(result)
