def solution(s):
    answer = []
    slice_s = s[2:-2]
    # 문자열에서 숫자만 뺌
    slice_s = slice_s.split("},{")
    # 집합의 순서를 정한다
    slice_s.sort(key = lambda x: len(x))
    store = {}

    for nums in slice_s:
        nums = nums.split(",")
        for n in nums:
            store[n] = 1
    
    for num in store:
        answer.append(int(num))
    answer = answer
    return answer

s = input()
print(solution(s))