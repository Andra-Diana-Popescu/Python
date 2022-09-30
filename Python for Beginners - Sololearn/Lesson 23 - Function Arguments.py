################################################################################
#####                                                                       ####
#####                     Lesson 23 - Function Arguments                    ####
#####                                                                       ####
################################################################################


# Example 1:

def print_with_exclamation(word):
    print(word + "!")

print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

# Example 2:

def print_double(x):
    print(2 * x)

print_double(3)

# Example 3:

def print_sum_twice(x, y):
    print(x + y)
    print(x + y)

print_sum_twice(5, 8)

# Example 4 :

def print_mult(x, y):
    print(x * y)

print_mult(2, 3)

################################################################################

# Practice 20 - From Feet to Inches

# You need to make a function that converts a foot value to inches.
# 1 foot has 12 inches. 
# Define a convert() function, that takes the foot value as argument and outputs the inches value.

################################################################################

# Solution:

feet = int(input())

def convert(ft):
    inches = ft * 12
    print(inches)

convert(feet)