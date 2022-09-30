################################################################################
#####                                                                       ####
#####                  Lesson 24 - Returning from Functions                 ####
#####                                                                       ####
################################################################################


# Example 1:

def max(x, y):
    if x >= y:
        return x
    else:
        return y

print(max(4, 7))

z = max(8, 5)
print(z)

# Example 2:

def shortest_string(x, y):
    if len(x) <= len(y):
        return x
    else:
        return y

print(shortest_string([1, 2, 3], [4, 5, 6, 7]))

# Example 3:

def add_numbers(x, y):
    total = x + y
    return total
    print("This won't be printed")

print(add_numbers(4, 5))

# Example 4:

def print_numbers():
    print(1)
    print(2)
    return
    print(4)
    print(6)

print_numbers()

################################################################################

# Practice 21 - How Many Letters

# Write a function that takes a string and a letter as its arguments and returns the count of the letter in the string.

# Sample Input

# hello, how are you?
# o

# Sample Output
# 3

# Explanation: The letter o appears 3 times in the given text.

################################################################################

# Solution:

text = str(input())
letter = str(input())

def letter_count(text, letter):
    return text.count(letter)

print(letter_count(text,letter))

################################################################################

# Practice 22 - Search Engine

# You’re working on a search engine. Watch your back Google!
# The given code takes a text and a word as input and passes them to a function called search().
# The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

# Sample Input

# "This is awesome"
# "awesome"

# Sample Output

# Word found

# Define the search() function, so that the given code works as expected.

################################################################################

# Solution:

text = input()
word = input()

def search(text, word):
    if word in text:
        return("Word found")
    else:
        return("Word not found")

print(search(text, word))