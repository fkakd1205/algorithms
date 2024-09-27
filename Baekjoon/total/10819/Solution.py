from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
answer = 0

for group in permutations(A, N):
    sum = 0
    for i in range(N-1):
        sum += abs(group[i] - group[i+1])

    answer = max(sum, answer)

print(answer)
