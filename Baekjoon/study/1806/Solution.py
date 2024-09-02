N, S = map(int, input().split())
arr = list(map(int, input().split()))

INF = int(1e9)
answer = INF
sum = 0
st = 0
en = 0
while st < N:
    while (en < N and sum < S):
        sum += arr[en]
        en += 1

    if sum >= S:
        answer = min(answer, en - st)
    if en > N:
        break
    sum -= arr[st]
    st += 1

if answer == INF:
    answer = 0
print(answer)
