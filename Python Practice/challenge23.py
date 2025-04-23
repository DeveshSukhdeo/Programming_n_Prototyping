# Devesh Sukhdeo 
# 4/23/25
# Period 1-2
# Python Coding Challenege 23

# Define function
def is_abecedarian(word):
    return list(word) == sorted(word)

# Test
print(is_abecedarian("abc"))       
print(is_abecedarian("aegilops"))  
print(is_abecedarian("art"))       
print(is_abecedarian("loop"))      

#List of words
words = ["abc", "aegilops", "art", "almost", "billowy", "biopsy", "chilly", "defy", "ghost", "loop"]
count = 0

#Count words
for word in words:
    if is_abecedarian(word):
        count += 1

# Print result 
print("Number of abecedarian words:", count)

