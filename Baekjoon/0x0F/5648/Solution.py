from sys import stdin

arr = list(map(int, stdin.readline().split()))
n = arr[0]
result = []

def revert(num):
    reverted_num = ''
    idx = 10
    while(True): 
        if(num == 0):
            return int(reverted_num)
        
        reverted_num += (str(num % 10))
        num = num // idx

if(len(arr)-1 < n):
    while(len(arr) <= n):
        temp = list(map(int, stdin.readline().split()))
        for num in temp:
            arr.append(num)

for num in arr[1:]:
    reverted_num = revert(num)
    result.append(reverted_num)

result.sort()
print(*result, sep="\n")
    