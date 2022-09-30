################################################################################
#####                                                                       ####
#####                      Lesson 3 - Exponentiation                        ####
#####                                                                       ####
################################################################################


print(2 ** 5)
print(5 ** 3)
print(2 ** 3 ** 2)
print(9 ** (1/2) )
print(27 ** (1/3) )
print(8 ** (1/3) )

################################################################################

# Practice 3 

# Did you know that there are more bacteria cells in your body than cells that make up your body? Weird!
# A bacteria culture starts with 500 bacteria and doubles in size every hour.
# Which means, after 1 hour the number of bacteria is 1000, after 2 hours - 2000, and so on.

# Let’s calculate and output the number of bacteria that will be in the culture after 24 hours.
# Write a program to calculate and output the answer.

# Hint: The formula to calculate the bacteria after N hours will be: 500 * 2ᴺ   

################################################################################

# Solution:

print(500 * (2 ** 24) )