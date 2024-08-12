N = int(input())
nums = list(map(int, input().split()))
answer = []
nums.sort()
en = N

if len(nums) % 2 == 1:
    answer.append(nums[-1])
    en = N-1

for i in range(en):
    j = en-1-i
    if i >= j: break
    answer.append(nums[i] + nums[j])

print(max(answer))
