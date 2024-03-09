from sys import stdin

T = int(input())

for _ in range(T):
    N, M = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))

    a.sort()
    b.sort()

    sum = 0
    b_idx = 0
    feed = 0
    # 이전에 먹힌 먹이들은 현재 a 보다 작은 먹이이므로, 먹힌 먹이 개수를 저장해 바로 더해준다
    for i in range(len(a)):
        while(b_idx < len(b) and b[b_idx] < a[i]):
            feed += 1
            b_idx += 1
        sum += feed
    
    print(sum)
