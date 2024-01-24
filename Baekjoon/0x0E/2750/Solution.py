from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

N = int(input())
arr = [int(stdin.readline()) for _ in range(N)]

# 버블 정렬
def bubble_sort():
    for i in range(N):
        for j in range(N-1-i):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

# 머지 소트
def merge_sort(st, en):
    if(st + 1 == en): return
    mid = (st + en) // 2
    merge_sort(st, mid)
    merge_sort(mid, en)
    merge(st, en)

temp = [0] * N
def merge(st, en):
    mid = (st + en) // 2
    lidx = st
    ridx = mid
    for i in range(st, en):
        if(lidx == mid):
            temp[i] = arr[ridx]
            ridx += 1
        elif(ridx == en):
            temp[i] = arr[lidx]
            lidx += 1
        elif(arr[lidx] <= arr[ridx]):
            temp[i] = arr[lidx]
            lidx += 1
        else:
            temp[i] = arr[ridx]
            ridx += 1
    for i in range(st, en):
        arr[i] = temp[i]

# 퀵 소트
def quick_sort(st, en):
    if(en <= st + 1): return
    pivot = arr[st]
    lidx = st + 1
    ridx = en - 1
    while(True):
        while(lidx <= ridx and arr[lidx] <= pivot): lidx += 1
        while(lidx <= ridx and arr[ridx] > pivot): ridx -= 1
        if(lidx > ridx): break
        temp = arr[lidx]
        arr[lidx] = arr[ridx]
        arr[ridx] = temp

    temp = arr[ridx]
    arr[ridx] = pivot
    arr[st] = temp

    quick_sort(st, ridx)
    quick_sort(ridx + 1, en)

# bubble_sort()
# merge_sort(0, N)
quick_sort(0, N)

print('\n'.join(map(str, arr)))
