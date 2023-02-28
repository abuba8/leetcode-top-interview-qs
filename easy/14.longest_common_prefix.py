def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    if len(strs) == 1:
        return strs[0]
    
    start = 1
    stac = []
    val = ''
    # stac.append(strs[0])
    strs_sort = sorted(strs, key=lambda l: (-len(l), l))
    
    while start < len(strs_sort):
        # print(strs_sort[start], strs_sort[0])
        for idx in range(len(strs_sort[start])):
            if strs_sort[start][idx] == strs_sort[0][idx]:
                val+=strs_sort[start][idx]
                print(val)
            else: break
        
        stac.append(val)
        val = ''
        
            
        start+=1
    print(stac)
    if len(set(stac)) == 1:
        return stac[0]
    else:
        return ""
    
    
    # common = ''
    # # strs_sort = sorted(strs, key=lambda l: (len(l), l))
    # for i in range(1, len(strs[0])+1):
    #     val = strs[0][:i]
    #     for j in range(1,len(strs)):
    #         print(val, strs[j][:i])
    #         if val == strs[j][:i]:
    #             common = val
    #         else:
    #             break
    
    # if common:
    #     return common
    # else:
    #     return ''
        
    
    # if len(strs) == 1:
    #     return strs[0]
    
    # strs_sort = sorted(strs, key=lambda l: (len(l), l))
    # common = ''
    # for i in range(1, len(strs_sort[0])+1):
    #     val = strs_sort[0][:i]
    #     for j in range(1,len(strs_sort)):
    #         if val in strs_sort[j]:
    #             common = val
    #         else:
    #             break
            
    # if common:
    #     return common
    # else:
    #     return ""
        
        
        
        
    
    
# x = longestCommonPrefix(["flower","flow","flight"])
# print(x)
# x = longestCommonPrefix(["dog","racecar","car"])
# print(x)
# x = longestCommonPrefix(["a"])
# print(x)
x = longestCommonPrefix(["aaa","aa","aaa"])
print(x)