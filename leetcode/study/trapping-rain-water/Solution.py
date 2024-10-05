from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        max_h = 0
        stack = []

        for h in height:
            if not stack:
                stack.append(h)
                max_h = h
                continue
            if h >= max_h:
                while stack:
                    answer += max_h - stack.pop()
                max_h = h
            stack.append(h)
        
        if stack:
            remain_h = reversed(stack)
            stack = []
            
            for h in remain_h:
                if not stack:
                    stack.append(h)
                    max_h = h
                    continue
                if h >= max_h:
                    while stack:
                        answer += max_h - stack.pop()
                    max_h = h
                stack.append(h)
        
        return answer

height = list(map(int, input().split()))
print(Solution().trap(height))