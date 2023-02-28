def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    
    if n == 0: return False
    
    while (n % 3) == 0:
        n = n/3
        if n == 1.0:
            return True
    else:
        return False
            
    # print('false')
            
    
x = isPowerOfThree(27)
print(x)
x = isPowerOfThree(0)
print(x)
x = isPowerOfThree(-1)
print(x)