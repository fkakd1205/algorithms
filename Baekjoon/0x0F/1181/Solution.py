from sys import stdin

N = int(input())
arr = [stdin.readline().rstrip() for _ in range(N)]

arr.sort(key = lambda x : (len(str(x)), x))

prev_word = ''
for i in range(N):
    if (prev_word != arr[i]):
        print(arr[i])
        prev_word = arr[i]
