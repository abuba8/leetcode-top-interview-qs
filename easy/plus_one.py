def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    val = int(''.join(str(x) for x in digits))
    return [int(x) for x in str(val+1)]
    
x = plusOne([1,2,3])
print(x)
x = plusOne([4,3,2,1])
print(x)
x = plusOne([9])
print(x)