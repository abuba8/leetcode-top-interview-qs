def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    for ch1, ch2 in zip(strs, strs[1:]):
        n = max(len(ch1), len(ch2))
        print(ch1, ch2)
        for i in range(n):
            # print(ch1,ch2)
            print(ch1[i], ch2[i])
        
        
        
    
    
longestCommonPrefix(["flower","flow","flight"])
# longestCommonPrefix(["dog","racecar","car"])