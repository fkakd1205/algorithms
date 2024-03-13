from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
count = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            count[i] = max(count[i], count[j] + 1)

print(max(count))
