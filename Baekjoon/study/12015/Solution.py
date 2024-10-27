N = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]

def binary_search(num):
    left = 0
    right = len(lis)

    while left <= right:
        mid = (left + right) // 2
        if lis[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    
    return right + 1

for i in range(1, N):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        idx = binary_search(arr[i])
        lis[idx] = arr[i]

print(len(lis))
