def solution(n, lost, reserve):
    answer = 0
    arr = [0] * (n+1)
    lost.sort()     # 오름차순 정렬. 앞 번호부터 체육복 가능 여부를 체크

    for l_num in lost:
        arr[l_num] -= 1

    for r_num in reserve:
        arr[r_num] += 1

    for l_num in lost:
        if arr[l_num] >= 0: continue
        if (l_num - 1 >= 1 and arr[l_num - 1] > 0):
            arr[l_num - 1] -= 1
            arr[l_num] += 1
        elif (l_num + 1 <= n and arr[l_num + 1] > 0):
            arr[l_num + 1] -= 1
            arr[l_num] += 1
    
    for i in range(1, n+1):
        if arr[i] >= 0: answer += 1

    return answer

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution(n, lost, reserve))
