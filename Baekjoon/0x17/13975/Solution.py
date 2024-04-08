from sys import stdin
from heapq import heappop, heappush

T = int(input())

for _ in range(T):
    K = int(stdin.readline().rstrip())
    nums = list(map(int, stdin.readline().split()))
    min_heap = []
    result = 0
    
    for n in nums:
        heappush(min_heap, n)
        
    
    for _ in range(K-1):
        a = heappop(min_heap)
        b = heappop(min_heap)
        sum = a + b
        result += sum
        heappush(min_heap, sum)

    print(result)
