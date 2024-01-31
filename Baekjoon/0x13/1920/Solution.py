from sys import stdin

N = int(input())
A = list(map(int, stdin.readline().split()))
M = int(input())
num = list(map(int, stdin.readline().split()))

A.sort()

def binary_search(target):
    st = 0
    en = N-1
    while(st <= en):
        mid = (st + en) // 2
        if(A[mid] < target):
            st = mid + 1
        elif(A[mid] > target):
            en = mid - 1
        else:
            return 1
    return 0

for n in num:
    print(binary_search(n))
