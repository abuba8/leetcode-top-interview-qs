def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    mapper = {'(': ')', '[': ']', '{': '}'}
    
    for i in range(len(s)):
        if s[i] in mapper:
            stack.append(s[i])
        elif stack and s[i] == mapper[stack[-1]]:
            stack.pop()
        else:
            return False
            
    if len(stack) == 0:
        return True
    else:
        return False