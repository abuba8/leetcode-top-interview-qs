class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if s == p:
            print('truee')
        
        if '*' in p:
            
            print('* or . here')
    
obj = Solution()
print(obj.isMatch('aa', 'a'))
print(obj.isMatch('aa', 'a*'))