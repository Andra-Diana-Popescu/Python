################################################################################
#####                                                                       ####
#####                  Lesson 25 - Comments and Docstrings                  ####
#####                                                                       ####
################################################################################

# Example 1:

x = 365
y = 7

# this is a comment

print (x % y) # find the remainder
# print (x // y)
# another comment

# Example 2:

x = 8
# printing x
print(x)

# Example 3:

def shout(word):
    """
    Print a word with an
    exclamation mark following
    it."""
    print(word + "!")

shout("spam")

help(shout) # you get the docstrings because it explains what the function does