N = int(input())

for i in range(2, N):
    if(i*i > N): break
    
    while(N % i == 0):
        print(i)
        N //= i

# 결과 N이 1이 아닌 경우는, 더 나눌 수 있는데 for문의 제한으로 출력되지 못한 것임
if(N != 1):
    print(N)
