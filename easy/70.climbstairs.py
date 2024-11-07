class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return b

obj = Solution()
print(obj.climbStairs(2))
print(obj.climbStairs(3))
print(obj.climbStairs(4))
print(obj.climbStairs(5))