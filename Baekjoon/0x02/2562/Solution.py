from sys import stdin

nums = dict()

for i in range(1, 10):
    num = int(stdin.readline().rstrip())
    nums[i] = num

nums = sorted(nums.items(), key=lambda x:x[1], reverse=True)

print(nums[0][1])
print(nums[0][0])
