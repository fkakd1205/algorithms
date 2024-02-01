from sys import stdin

N, M = map(int, input().split())
A = list(map(int, stdin.readline().split()))

st = 0
en = 0
count = 0
while(en <= N):
    temp = sum(A[st:en])
    if(temp == M):
        count += 1
        en += 1
    elif(temp < M):
        en += 1
    else:
        st += 1

print(count)
