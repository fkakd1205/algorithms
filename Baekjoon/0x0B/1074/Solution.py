N, r, c = map(int, input().split())

result = 0

while(N > 0):
    # 현재 배열의 r, c크기
    size = 2 ** N
    # 배열의 몇사분면에 있는지 확인하기 위한 비교 값
    temp = size // 2

    if (r < temp and c < temp):     # 2사분면
        result += 0
    elif (r < temp and c >= temp):      # 1사분면
        result += temp * temp
        c -= temp
    elif (r >= temp and c < temp):      # 3사분면
        result += temp * temp * 2
        r -= temp
    elif (r >= temp and c >= temp):     # 4사분면
        result += temp * temp * 3
        r -= temp
        c -= temp
    N -= 1

print(result)
