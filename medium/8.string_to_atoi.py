def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    
    s = s.strip()
    s = s.split()
    num = ''
    if s[0].isalpha(): return 0
    
    # print(int(float(s[0])))
    
    if int(float(s[0])) >= 2 ** 31 or int(float(s[0])) <= (-2 ** 31) - 1:
        if int(float(s[0])) < 0: return -2 ** 31
        else: return 2 ** 31
    
    if len(s) == 1:
        num = int(float(s[0]))
    else:
        try:
            num = int(float(s[0]))
        except:
            pass
           
    return num


# x = myAtoi("42")
# print(x)
# x = myAtoi("          -42")
# print(x)
# x = myAtoi("4193 with words")
# print(x)
# x = myAtoi("words and 987")
# print(x)
# x = myAtoi("-91283472332")
# print(x)
# x = myAtoi("3.14159")
# print(x)
x = myAtoi("+-12")
print(x)