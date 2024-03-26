from sys import stdin

# x + y = z - k
N = int(input())
nums = [int(stdin.readline().rstrip()) for _ in range(N)]
nums.sort()
sum_arr = set()

for x in nums:
    for y in nums:
        sum_arr.add(x+y)

def func():
    for i in range(N-1, -1, -1):
        for j in range(i):
            if (nums[i] - nums[j]) in sum_arr:
                return nums[i]
            
print(func())
