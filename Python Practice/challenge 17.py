# Devesh Sukhdeo
# 4/4/25
# Period 1-2
# Python Coding Challenge 17

# Define a function named is_power that takes two parameters: a and b.
# This function checks if 'a' is a power of 'b'.
def is_power(a, b):
    # Base case: if a is smaller than b, it cannot be a power of b.
    if a < b:
        return False

    # Base case: if a equals b, return True because a is b^1.
    if a == b:
        return True

    # Recursive case: check if a is divisible by b.
    if a % b == 0:
        #If a is divisible by b, divide a by b and recursively check if the quotient is also a power of b.
        return is_power(a / b, b)

    # If a is not divisible by b, return False because a cannot be a power of b.
    return False

# Test cases:
print("Test 1:", is_power(16, 2))  # Expected True
print("Test 2:", is_power(27, 3))  # Expected True
print("Test 3:", is_power(9, 2))   # Expected False
print("Test 4:", is_power(81, 3))  # Expected True
print("Test 5:", is_power(32, 5))  # Expected False

