from sys import stdin
from copy import deepcopy

N = int(input())
X = list(map(int, stdin.readline().split()))

# temp1 : 정렬된 X, temp2 : 중복제거된 temp1
temp1 = deepcopy(X)
temp1.sort()
temp2 = []

# 중복 제거
for i in range(len(temp1)):
    if((not temp2) or temp1[i-1] != temp1[i]):
        temp2.append(temp1[i])

def binary_search(target):
    st = 0
    en = len(temp2)-1

    while(st <= en):
        mid = (st + en) // 2
        if(temp2[mid] < target): st = mid + 1
        elif(temp2[mid] > target): en = mid - 1
        else: return mid
    return 0

result = []
for target in X:
    result.append(binary_search(target))

print(*result)    
