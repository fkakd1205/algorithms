N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]

answer = []
idx = 0
for _ in range(N):
    idx = (idx + (K-1)) % len(arr)
    answer.append(str(arr.pop(idx)))

print("<", ", ".join(answer), ">", sep="")
