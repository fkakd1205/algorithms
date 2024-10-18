from sys import stdin

INF = int(1e9)
N = int(input())
nums = list(map(int, stdin.readline().split()))
operations = list(map(int, stdin.readline().split()))
mn = INF
mx = -INF

def brute_force(cur, sum):
    global mn, mx

    if cur == N-1:
        mn = min(mn, sum)
        mx = max(mx, sum)
        return
    
    if operations[0] != 0:
        operations[0] -= 1
        brute_force(cur+1, sum + nums[cur+1])
        operations[0] += 1
    
    if operations[1] != 0:
        operations[1] -= 1
        brute_force(cur+1, sum - nums[cur+1])
        operations[1] += 1
    
    if operations[2] != 0:
        operations[2] -= 1
        brute_force(cur+1, sum * nums[cur+1])
        operations[2] += 1
        
    if operations[3] != 0:
        operations[3] -= 1
        result = 0
        if sum < 0:
            result = -(-sum // nums[cur+1])
        else:
            result = sum // nums[cur+1]
        brute_force(cur+1, result)
        operations[3] += 1

brute_force(0, nums[0])

print(mx)
print(mn)
