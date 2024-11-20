class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        start = 0
        end = len(heights) - 1
        val = 0
        if len(heights) == 1: return heights[0]
        
        while start <= end:
            print(heights[start], heights[end])
            print(min(heights[start:end+1]), ((end-start)+1))
            print(min(heights[start:end+1]) * ((end-start)+1))
            print('-----------------------')
            area = (min(heights[start:end+1])) * ((end-start)+1)
            if val < area: val = area
            if heights[start] <= heights[end]: start+=1
            else: end-=1
        return val

obj = Solution()
# print(largestRectangleArea([1]))
# print(largestRectangleArea([0,9]))
print(obj.largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))