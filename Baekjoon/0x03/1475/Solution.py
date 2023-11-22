N = input()
arr = [0 for _ in range(10)]

for i in N:
    num = int(i)
    if(num == 6 or num == 9):
        if(arr[6] < arr[9]) : arr[6] += 1
        else: arr[9] += 1
    else:
        arr[num] += 1

arr.sort()
print(arr[-1])
