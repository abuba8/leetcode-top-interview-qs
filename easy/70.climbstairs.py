def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    print(b)
    
climbStairs(2)
climbStairs(3)
climbStairs(4)
climbStairs(5)