from sys import stdin

# V1. quick sort 시간초과
# N = int(input())
# arr = [int(stdin.readline().rstrip()) for _ in range(N)]

# def quick_sort(st, en):
#     if(st + 1 >= en): return
#     pivot = arr[st]
#     lidx = st + 1
#     ridx = en - 1
#     while(True):
#         while(lidx <= ridx and arr[lidx] >= pivot): lidx += 1
#         while(lidx <= ridx and arr[ridx] <= pivot): ridx -= 1
#         if(lidx > ridx): break
#         arr[lidx], arr[ridx] = arr[ridx], arr[lidx]
#     arr[ridx], arr[st] = arr[st], arr[ridx]
#     quick_sort(st, ridx)
#     quick_sort(ridx + 1, en)

# quick_sort(0, N)
# print(*arr, sep="\n")

# V2. 배열사용
N = int(input())
nums = [0] * 2000005

for _ in range(N):
    n = int(stdin.readline().rstrip())
    nums[n + 1000000] += 1

for i in range(len(nums)-1, -1, -1):
    if(nums[i] == 0): continue
    print(i - 1000000)
