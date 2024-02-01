N = int(input())

is_prime = [False, False] + [True] * (N-1)
arr = []

# 1. 소수 판별
for i in range(2, N+1):
    if(i * i > N): break

    for j in range(i*i, N+1, i):
        is_prime[j] = False

for i in range(N+1):
    if(is_prime[i]):
        arr.append(i)

# 2. 연속된 소수 합으로 N을 만들 수 있는지 확인
def solve():
    count = 0
    st = 0
    en = 0
    while(en <= len(arr)):
        temp = sum(arr[st:en])
        if(temp == N):
            count += 1
            en += 1
        elif(temp < N):
            en += 1
        else:
            st += 1
        
    return count

result = 0
if(arr):
   result = solve()

print(result)
