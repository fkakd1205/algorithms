N = int(input())

for _ in range(N):
    a, b = map(sorted, input().split())
    result = "Possible" if(a == b) else "Impossible"
    print(result)
