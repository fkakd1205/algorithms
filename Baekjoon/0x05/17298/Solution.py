from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
stack = [0]
result = [-1] * N

for i in range(1, N):
    # 스택에 남아있는 수 중 현재 수보다 작은수가 존재한다면 오큰수 업데이트
    while(stack and arr[stack[-1]] < arr[i]):
        result[stack.pop()] = arr[i]
    # 원소의 인덱스를 넣는다
    stack.append(i)

print(*result)
