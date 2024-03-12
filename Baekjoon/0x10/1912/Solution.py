from sys import stdin

n = int(input())
arr = list(map(int, stdin.readline().split()))
sum = [0] * n
sum[0] = arr[0]

for i in range(1, n):
    sum[i] = max(sum[i-1] + arr[i], arr[i])

print(max(sum))
