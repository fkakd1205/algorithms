N = int(input())
M = int(input())
broken = list(map(int, input().split()))

# 500000이 아닌 2배를 한 이유는
# 예를 들어, MAX가 100이고 현재 채널이 0일때 +100(100번) vs 150-50(3번 + 50번)
# 따라서 150으로 이동하는 것이 더 효율적
MAX = 500_000 * 2
mn = abs(100-N)

for num in range(MAX):
    nums = str(num)
    # 해당 num을 만들 수 있는지 검사
    for i in range(len(nums)):
        if int(nums[i]) in broken: break
        if len(nums)-1 == i:
            mn = min(mn, abs(num-N) + len(nums))

print(mn)
