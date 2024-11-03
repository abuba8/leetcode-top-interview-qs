class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapper = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        val = 0
        val += mapper.get(s[0])
        
        for ix1, ix2 in zip(s, s[1:]):
            val+=mapper.get(ix2)
            if ix1 == 'I' and (ix2 == 'V' or ix2 =='X'):
                val = val - 2
            elif ix1 == 'X' and (ix2 == 'L' or ix2 =='C'):
                val = val - 20
            elif ix1 == 'C' and (ix2 == 'D' or ix2 =='M'):
                val = val - 200
                     
        return val
        
obj = Solution()    
print(obj.romanToInt("III"))
print(obj.romanToInt("LVIII"))
print(obj.romanToInt("MCMXCIV"))