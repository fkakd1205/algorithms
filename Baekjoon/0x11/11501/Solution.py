from sys import stdin

T = int(input())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().split()))
    
    idx = N-1
    sum = 0
    comp_idx = idx-1
    while(idx > 0 and comp_idx >= 0):
        if arr[comp_idx] <= arr[idx]:
            sum += (arr[idx] - arr[comp_idx])
            comp_idx -= 1
        else:
            idx = comp_idx

    print(sum)