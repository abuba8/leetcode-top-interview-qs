def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    
    if s == p:
        print('truee')
    
    if '*' in p:
        
        print('* or . here')
    

isMatch('aa', 'a')
isMatch('aa', 'a*')