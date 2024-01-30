from sys import stdin

N = int(input())
num = list(map(int, stdin.readline().split()))
cnt = 0

def is_prime(n):
    if(n == 1): return False

    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True        

for n in num:
    if(is_prime(n)):
        cnt += 1

print(cnt)
