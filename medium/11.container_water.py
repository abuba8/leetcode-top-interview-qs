class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        val = 0
        
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            if val < area: val = area
            if height[start] < height[end]: start+=1
            else: end-=1
        return val
       
        
obj = Solution()
print(obj.maxArea([2,3,4,5,18,17,6]))