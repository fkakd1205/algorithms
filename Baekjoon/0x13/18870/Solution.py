from sys import stdin

N = int(input())
X = list(map(int, stdin.readline().split()))

# temp : 중복제거, 정렬된 X
temp = list(set(X))
temp.sort()

def binary_search(target):
    st = 0
    en = len(temp)-1

    while(st <= en):
        mid = (st + en) // 2
        if(temp[mid] < target): st = mid + 1
        elif(temp[mid] > target): en = mid - 1
        else: return mid
    return 0

result = []
for target in X:
    result.append(binary_search(target))

print(*result)    
