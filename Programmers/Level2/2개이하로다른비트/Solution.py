def solution(numbers):
    answer = []
    for num in numbers:
        arr = ['0'] + list(map(str, bin(num)[2:]))
        # 짝수는 0으로 끝난다 -> 마지막 비트를 1로 바꾸기
        # 홀수는 1로 끝난다 -> 마지막 0의 인덱스 k를 찾아서, k번째를 1로 바꾸고 k+1번째를 0으로 바꾼다.
        if num % 2 == 0:
            arr[-1] = '1'
        else:
            zero_idx = -1
            for idx in range(len(arr)):
                if arr[idx] == '0':
                    zero_idx = idx
            
            arr[zero_idx] = '1'
            arr[zero_idx+1] = '0'
        
        res = ''.join(arr)
        answer.append(int(res, 2))
    return answer

numbers = list(map(int, input().split()))
print(solution(numbers))
