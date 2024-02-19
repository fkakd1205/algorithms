n, k = map(int, input().split())
nums = [i for i in range(1, n+1)]

result = []
cur = 0
while nums:
    cur = (cur - 1 + k) % len(nums)
    result.append(nums.pop(cur))

print('<', end='')
print(*result, sep=', ', end='')
print('>')

