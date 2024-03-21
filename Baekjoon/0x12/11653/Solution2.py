N = int(input())

for i in range(2, N):
    # 더이상 나눠질 수 없다면
    if(i * i > N): break

    while(N % i == 0):
        print(i)
        N //= i

if N != 1:
    print(N)
