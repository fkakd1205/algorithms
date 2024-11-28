st, en = map(int, input().split())
nn_squre = [True] * (en+1-st)

for i in range(2, en+1):
    if i * i > en: break
    div = i ** 2
    
    # st ~ en에서 div의 배수를 찾기 위한 값
    # ex. i = 2, 103 ~ 200일 때, (103 // 2**2) * (2**2) = 100을 찾고, for문에서 st ~ en까지 범위를 맞춘다
    temp = (st // div) * div

    for j in range(temp, en+1, div):
        if j < st: continue
        nn_squre[j-st] = False

print(sum(nn_squre)) 
