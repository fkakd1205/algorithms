from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
result = 0

# A는 오름차순, B는 내림차순 정렬. (B의 큰 수와 A의 작은 수가 곱해져야 전체 합이 작아짐)
A.sort()
B.sort(reverse=True)

for i in range(N):
    result += A[i] * B[i]

print(result)
