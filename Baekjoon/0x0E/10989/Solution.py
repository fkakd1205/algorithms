from sys import stdin

# V1. 메모리초과
# N = int(input())
# nums = [int(stdin.readline().rstrip()) for _ in range(N)]

# # quick sort
# # 1. pivot을 기준으로 작은 값은 왼쪽, 큰 값은 오른쪽에 배치
# # 2. 작은 값을 가리키는 idx, 큰 값을 가리키는 idx가 교차되었다면 pivot과 자리 바꿔주고
# # 3. pivot을 기준으로 왼쪽 배열, 오른쪽 배열을 분리해 정렬

# def quick_sort(st, en):
#     if(st + 1 >= en): return
#     pivot = nums[st]
#     lidx = st + 1
#     ridx = en - 1
#     while(True):
#         while(lidx <= ridx and nums[lidx] <= pivot): lidx += 1
#         while(lidx <= ridx and nums[ridx] >= pivot): ridx -= 1
#         if(lidx > ridx): break
#         nums[lidx], nums[ridx] = nums[ridx], nums[lidx]
#     nums[ridx], nums[st] = nums[st], nums[ridx]
#     quick_sort(st, ridx)
#     quick_sort(ridx+1, en)

# quick_sort(0, N)
# print(*nums, sep="\n")

N = int(input())
arr = [0] * 10001

for _ in range(N):
    num = int(stdin.readline().rstrip())
    arr[num] += 1

for i in range(len(arr)):
    if(arr[i] > 0):
        for j in range(arr[i]):
            print(i)
