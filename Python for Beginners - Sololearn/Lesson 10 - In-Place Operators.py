################################################################################
#####                                                                       ####
#####                     Lesson 10 - In-Place Operators                    ####
#####                                                                       ####
################################################################################


# Example 1:

x = 2
print(x)

# Example 2:
# x = x + 3

x += 3
print(x)

# Example 3:

x = 4
x *= 3
print(x)

# Example 4:

x = "hello"
print(x)

x += "world"
print(x)

# Example 5:

x = "hey"
x *= 3
print(x)

################################################################################

# Practice 8 

# When you go out to eat, you always tip 20% of the bill amount.
# But who’s got the time to calculate the right tip amount every time? 
# Not you that’s for sure! You’re making a program to calculate tips and save some time.

# Your program needs to take the bill amount as input and output the tip.

# Sample Input
# 50

# Sample Output
# 10.0

# Hint:
# Explanation: 20% of 50 is 10. 
# To calculate 20% of a given amount, you can multiply the number by 20 and divide it by 100: 50*20/100 = 10.0

################################################################################

# Solution:

bill=int(input())
print(bill * 20/100)