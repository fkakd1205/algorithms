def solution(nums):
    store = {}
    answer = 0
    pick_cnt = len(nums) // 2

    for n in nums:
        if n in store:
            store[n] += 1
        else:
            store[n] = 0
    
    if len(store) >= pick_cnt:
        answer = pick_cnt
    else:
        answer = len(store)

    return answer

arr = input().split()
print(solution(arr))