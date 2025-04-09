# Devesh Sukhdeo 
# Period 1-2
# 4/8/25
# Python Coding Challenge 19

# Define a function named has_no_e that checks if a word contains the letter 'e'
def has_no_e(word):
    # Loop through each letter in the given word
    for letter in word:
        # If the letter 'e' is found, return False (meaning the word contains 'e')
        if letter == 'e':
            return False
    # If the loop completes without finding 'e', return True (word does not contain 'e')
    return True

# Define a function named filter_words_without_e that processes a list of words
def filter_words_without_e(words):
    # Create a new list that only includes words that do not contain the letter 'e'
    words_without_e = [word for word in words if has_no_e(word)]
    
    # Count the total number of words in the original list
    total_words = len(words)
    
    # Count how many words do not contain the letter 'e'
    count_without_e = len(words_without_e)
    
    # Calculate the percentage of words that do not contain 'e'
    if total_words == 0:
        # If the total number of words is zero, set the percentage to zero to avoid division errors
        percentage = 0.0
    else:
        percentage = (count_without_e / total_words) * 100

    # Print the list of words that do not contain 'e'
    print(f"Words without 'e': {words_without_e}")
    
    # Print the calculated percentage with two decimal places for clarity
    print(f"Percentage of words without 'e': {percentage:.2f}%")

# Define a sample list of words to test the function
sample_words = ["apple", "banana", "sky", "cloud", "tree", "mountain", "sun", "grass"]

# Call the function and pass the sample word list to see the output
filter_words_without_e(sample_words)


