from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = 0
        size = len(heights)
        stack = []

        # 증가하면 stack에 추가. 감소하면 현재 stack의 마지막 요소를 꺼내 비교
        for i in range(size):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                # 현재 height로 너비를 결정하는 값은 남아있는 stack의 값을 참고
                width = i if not stack else i - stack[-1] - 1
                answer = max(answer, width * height)
            stack.append(i)
        
        # stack에 남아있다는 건, 증가하며 쌓인 히스토그램
        while stack:
            height = heights[stack.pop()]
            width = size if not stack else size - stack[-1] - 1
            answer = max(answer, width * height)
        return answer

heights = list(map(int, input().split()))
print(Solution().largestRectangleArea(heights))
