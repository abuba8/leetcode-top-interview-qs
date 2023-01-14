def mySqrt(x):
    if x < 0:
        raise ValueError("Input should be non-negative")
    elif x == 0 or x == 1:
        return x
    else:
        # Start with an initial guess
        guess = x / 2
        # Keep refining the guess until it is accurate enough
        while abs(guess * guess - x) > 0.0001:
            guess = (guess + x / guess) / 2
        return int(guess)

x = mySqrt(4)
print(x)
x = mySqrt(8)
print(x)
