N = int(input())
arr = list(map(int, input().split()))

INF = int(2e9)
arr.sort()
left = 0
right = len(arr)-1
diff = INF
answer = arr[left], arr[right]

while True:
    if left >= right: break
    
    sum = arr[left] + arr[right]
    if abs(sum) < diff:
        answer = arr[left], arr[right]
        diff = abs(sum)
    
    if sum == 0:
        break
    elif sum < 0:
        left += 1
    else:
        right -= 1

print(*answer)
