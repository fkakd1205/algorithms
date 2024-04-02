from sys import stdin

N, K = map(int, input().split())
arr = list(map(int, stdin.readline().split()))

en = 0
odd_cnt = 0
even_cnt = 0
mx = 0

for st in range(N):
    while(odd_cnt <= K and en < N):
        if (arr[en] % 2 != 0):
            odd_cnt += 1
        else:
            even_cnt += 1
        en += 1

    mx = max(mx, even_cnt)
    if en == N: break

    if (arr[st] % 2 != 0):
        odd_cnt -= 1
    else:
        even_cnt -= 1

print(mx)