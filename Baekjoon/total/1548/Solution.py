from sys import stdin

N = int(input())
arr = list(map(int, stdin.readline().split()))
arr.sort()
mx = 0

for i in range(N-2):
    for j in range(N-1, i+1, -1):
        if arr[i] + arr[i+1] > arr[j]:
            mx = max(mx, j - i + 1)
            break

if mx == 0:
    mx = min(2, N)

print(mx)
