n = int(input())
nums = list(map(int, input().split()))
v = int(input())

count = 0
for n in nums:
    if n == v:
        count += 1

print(count)
