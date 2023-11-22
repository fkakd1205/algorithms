N, X = map(int, input().split())
array = list(map(int, input().split()))

for i in range(N):
    if(array[i] < X):
        print(array[i], end = " ")

