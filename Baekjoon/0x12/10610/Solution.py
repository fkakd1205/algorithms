# 배수 판정법
# 3의 배수는 각 자리수의 합이 3이면 3의 배수이다.
nums = list(map(int, input()))

if 0 not in nums: print(-1)
else:
    s = sum(nums)
    if s % 3 == 0:
        nums.sort(reverse=True)
        print(*nums, sep='')
    else:
        print(-1)
