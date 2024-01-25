from sys import stdin

T = int(input())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))
    A.sort()
    B.sort()
    count = 0
    result = 0

    # A를 기준으로 탐색
    for i in range(N):
        while True:
            # 탐색된 B의 모든 원소가 A[i]의 원소보다 작은 경우 (count == M)
            # A[i]의 원소가 탐색되지 않은 B의 원소보다 작거나 같은 경우 (A[i] <= B[count])
            # count는 누적되어 더해짐. A[i-1]의 원소는 A[i]의 원소보다 작으므로
            if count == M or A[i] <= B[count]:
                result += count
                break
            else:
                count += 1

    print(result)
