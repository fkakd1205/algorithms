arr = list(input().split('-'))
answer = 0

for i in range(len(arr)):
    nums = list(map(int, arr[i].split('+')))
    if i == 0:
        answer += sum(nums)
    else:
        answer -= sum(nums)

print(answer)
