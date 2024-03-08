from sys import stdin

# V1.
# N = int(input())
# arr = [list(map(int, stdin.readline().split())) for _ in range(N)]

# arr.sort(key = lambda x : (x[0], x[1]))
# print(arr)

# V2. merge sort
N = int(input())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
temp = [0] * N

def merge(st, en):
    global arr

    mid = (st + en) // 2
    lidx = st
    ridx = mid
    for i in range(st, en):
        if (lidx == mid):
            temp[i] = arr[ridx]
            ridx += 1
        elif (ridx == en):
            temp[i] = arr[lidx]
            lidx += 1
        elif (arr[lidx][0] <= arr[ridx][0]):
            if (arr[lidx][0] == arr[ridx][0] and arr[lidx][1] > arr[ridx][1]):
                temp[i] = arr[ridx]
                ridx += 1
                continue
            temp[i] = arr[lidx]
            lidx += 1
        else:
            temp[i] = arr[ridx]
            ridx += 1
        
    for i in range(st, en):
        arr[i] = temp[i]

def merge_sort(st, en):
    if (st + 1 >= en): return
    mid = (st + en) // 2
    merge_sort(st, mid)
    merge_sort(mid, en)
    merge(st, en)

merge_sort(0, N)
for x, y in arr:
    print(x, y)
