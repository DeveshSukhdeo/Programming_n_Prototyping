# Devesh Sukhdeo 
# Period 1-2
# 4/2/25
# Python Coding Challenge 16

#Return first letter
def first_letter(word):
    return word[0] 

#Return last letter
def last_letter(word):
    return word[-1] 

#Return middle part
def middle_part(word):
    return word[1:-1]

#Palindrome checker 
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first_letter(word) == last_letter(word):
        return is_palindrome(middle_part(word))
    return False

#Check
print(is_palindrome("noon"))        # Expected output: True
print(is_palindrome("redivider"))   # Expected output: True
print(is_palindrome("hello"))       # Expected output: False
print(is_palindrome("a"))           # Expected output: True
print(is_palindrome(""))            # Expected output: True

