class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        a = 0
        b = len(heights) - 1
        maxArea = 0

        while a < b:
            h = min(heights[a], heights[b])
            area = (b - a) * h
            maxArea = max(area, maxArea)
            if h == heights[a]:
                a += 1
            else:
                b -= 1
            
        
        return maxArea
