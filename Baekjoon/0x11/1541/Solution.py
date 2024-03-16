# -로 구분된 수들을 합하면 큰 값으로 뺴줄 수 있다 (-다음 +가 나온 경우 큰 값으로 빼줄 수 있다)
exp = input().split('-')

answer = 0
for i in range(len(exp)):
    arr = exp[i].split('+')
    
    sum = 0
    for n in arr:
        sum += int(n)
    if(i == 0):
        answer += sum
    else:
        answer -= sum

print(answer)
