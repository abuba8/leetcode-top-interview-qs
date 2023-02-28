def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    s[:] = s[::-1]
    return s
   
    
x = reverseString(["h","e","l","l","o"])
print(x)
x = reverseString(["H","a","n","n","a","h"])
print(x)
