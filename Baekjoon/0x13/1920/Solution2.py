from sys import stdin

N = int(input())
nums = list(map(int, stdin.readline().split()))
nums.sort()

M = int(input())
target = list(map(int, stdin.readline().split()))

def binary_search(t):
    st = 0
    en = N-1
    while(st <= en):
        mid = (st + en) // 2
        if nums[mid] < t: st = mid + 1
        elif nums[mid] > t: en = mid - 1
        else: return 1
    return 0

for t in target:
    print(binary_search(t))
