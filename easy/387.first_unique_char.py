def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    
    mapper = []
    for i in s:
        mapper.append((i, s.count(i)))
    mapper = sorted(mapper, key=lambda x: x[1])
    
    for item in mapper:
        if item[1] == 1:
            return s.index(item[0])
    
    return -1
             
    
x = firstUniqChar("leetcode")
print(x)
x = firstUniqChar("loveleetcode")
print(x)
x = firstUniqChar("aabb")
print(x)