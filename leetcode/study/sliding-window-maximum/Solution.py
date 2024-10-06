from typing import List
from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        st = 0
        en = k
        max_heap = []

        for i in range(k):
            heappush(max_heap, (-nums[i], i))
        
        while True:
            while max_heap[0][1] < st:
                heappop(max_heap)
                
            answer.append(-max_heap[0][0])

            if en >= len(nums):
                break

            heappush(max_heap, (-nums[en], en))
            st += 1
            en += 1
        return answer

nums = list(map(int, input().split()))
k = int(input())
print(Solution().maxSlidingWindow(nums, k))
