def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    s = [str(x) for x in s]
    s = '"' + '","'.join(s) + '"'

    return s[::-1]   
    
x = reverseString(["h","e","l","l","o"])
print(x)
x = reverseString(["H","a","n","n","a","h"])
print(x)
