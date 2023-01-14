def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # print(s, t[::-1])
    if sorted(s) == sorted(t):
        return True
    else:
        return False
    
x = isAnagram("anagram", "nagaram")
print(x)
x = isAnagram("rat", "car")
print(x)