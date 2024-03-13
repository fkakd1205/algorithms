from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
sum = [0] * N
sum[0] = arr[0]

for i in range(1, N):
    for j in range(N):
        if arr[j] < arr[i]:
            sum[i] = max(sum[i], sum[j] + arr[i])
        else:
            sum[i] = max(sum[i], arr[i])
    
print(max(sum))
