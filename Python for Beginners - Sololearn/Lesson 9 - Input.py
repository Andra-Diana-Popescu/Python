################################################################################
#####                                                                       ####
#####                          Lesson 9 - Input                             ####
#####                                                                       ####
################################################################################


# input()

x = input()
print(x)

# Take the user input, assign it to a variable and output it:

text = input()
print(text)

name = input("Enter your name: ")
print("Hello, " + name)

# str()

age = 42
print("His age is "  + str(age))

# int()

age = int(input())
print(age)

################################################################################

# Practice 7 

# Write a program to add 3 stars at the beginning and the end of the notification text.

################################################################################

# Solution:

quote = input ("Enter a quote:")
print("***" + quote + " ***")