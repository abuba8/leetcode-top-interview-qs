def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    
    if s == ' ':
        return True
    
    val = ''.join(ch for ch in s.strip().lower() if ch.isalnum())
    
    if val == val[::-1]:
        return True
    else:
        return False

    
x = isPalindrome("A man, a plan, a canal: Panama")
print(x)
x = isPalindrome("race a car")
print(x)
x = isPalindrome(" ")
print(x)