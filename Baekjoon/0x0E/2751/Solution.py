from sys import stdin

N = int(input())
nums = [int(stdin.readline().rstrip()) for _ in range(N)]
temp = [0] * N

# merge sort
# 1. 분리한다
# 2. 비교한다
# 3. 합친다

def merge(st, en):
    mid = (st + en) // 2
    lidx = st
    ridx = mid
    
    for i in range(st, en):
        if (lidx == mid):
            temp[i] = nums[ridx]
            ridx += 1
        elif (ridx == en):
            temp[i] = nums[lidx]
            lidx += 1
        elif (nums[lidx] <= nums[ridx]):
            temp[i] = nums[lidx]
            lidx += 1
        else:
            temp[i] = nums[ridx]
            ridx += 1

    for i in range(st, en):
        nums[i] = temp[i]
    
def merge_sort(st, en):
    if(st + 1 == en): return
    mid = (st + en) // 2
    merge_sort(st, mid)
    merge_sort(mid, en)
    merge(st, en)

merge_sort(0, N)
print(*nums, sep="\n")
