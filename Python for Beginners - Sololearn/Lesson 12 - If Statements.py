################################################################################
#####                                                                       ####
#####                        Lesson 12 - If Statements                      ####
#####                                                                       ####
################################################################################


# if condition:
#    statements

# Example 1:

x = 42
if x > 5:
    print("x is greater than 5")

# Example 2:

spam = 7
if spam > 5:
    print("five")
    if spam > 8:
        print("eight")

# Example 3:

num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 5 and 47")

# Example 4:

num = 7
if num > 3:
    print("3")
    if num < 5:
        print("5")
        if num == 7:
            print("7")

################################################################################

# Practice 9 

# You’re making a gold purity checker, that should accept only 22K or 24K gold. Only the good stuff!
# 22K gold has 91.7% or more gold in it, while 24K corresponds to 99.9% and above purity.
# Given the % of gold purity as input, you should output "Accepted" only if it corresponds to 22 or 24K.
# Note: Less than 91.7 purity should output nothing.

# Sample Input:
# 93.4

# Sample Output:
# Accepted

################################################################################

# Solution:

purity = float(input())
if purity >= 91.7:
    print("Accepted")