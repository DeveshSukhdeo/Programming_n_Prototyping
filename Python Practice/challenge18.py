# Devesh Sukhdeo
# Period 1-2
# 4/7/25
# Python Coding Challenge 18 

# Define the function `gcd` which takes two parameters `a` and `b`.
# The function calculates the greatest common divisor (GCD) of `a` and `b`.
def gcd(a, b):
    # Base case: If `b` is 0, return `a` because the GCD of any number and 0 is the number itself.
    if b == 0:
        return a
    # Recursive case: If `b` is not 0, calculate the remainder of `a` divided by `b`.
    # Then recursively call `gcd` with `b` and the remainder of `a % b`.
    else: 
        return gcd(b, a % b)

# Test cases:
print("GCD of 48 and 18 is:", gcd(48, 18))     # Expected: 6
print("GCD of 56 and 98 is:", gcd(56, 98))     # Expected: 14
print("GCD of 101 and 10 is:", gcd(101, 10))   # Expected: 1
print("GCD of 42 and 56 is:", gcd(42, 56))     # Expected: 14
print("GCD of 17 and 13 is:", gcd(17, 13))     # Expected: 1

