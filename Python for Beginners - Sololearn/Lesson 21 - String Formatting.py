################################################################################
#####                                                                       ####
#####                       Lesson 21 - String Formatting                   ####
#####                                                                       ####
################################################################################


# format() - Enables values to be embedded in it, using placeholders

# Example 1:

name = "Andra"
age = 26

msg = ("My name is {} and my age is {} years old.").format(name,age)

print(msg)

# Example 2:

name = "Christian"
age = 27

msg = ("My name is {} and my age is {} years old. My weight is {} kg and my height is {} feets. My favourite game is {}.").format(name,age,71,5.8,"Cricket")

print(msg)

# Example 3:

msg = ("My name is {my_name} and my age is {my_age} years old.").format(my_name = name, my_age = age)

print(msg)

# Example 4:

msg = "Numbers: {}, {}, {}".format(42, 50, 90)

print(msg)

# Example 5:

msg = "Numbers: {0}, {1}, {2}".format(42, 50, 90)

print(msg)

# Example 6:

msg = "Numbers: {2}, {0}, {1}".format(42, 50, 90)

print(msg)

# Example 5:

nums = [4, 5, 6]

msg = "Numbers: {0}, {1}, {2}".format(nums[2], nums[0], nums[1])

print(msg)

# Example 6:

print("{0}{1}{0}".format("abra", "cad"))

# Example 7:

a = "{x}, {y}".format(x = 5, y = 12)
print(a)

# Example 8:

my_numbers = "{c}, {b}, {a}".format(a = 5, b = 9, c = 7)
print(my_numbers)

# Other useful string functions:

# join - Joins a list of strings with another string as a separator

print(", ".join(["spam", "eggs", "ham"]))

# split - The opposite of join, turns a string with a certain separator into a list

print("spam, eggs, ham".split(", "))

# replace - Replaces one substring in a string with another

print("Hello ME".replace("ME", "world!"))

# startswith - Determines if there is a substring at the start of a string

print("This is a sentence.".startswith("This"))

# endswith - Determines if there is a substring at the end of a string

print("This is a sentence.".endswith("sentence."))

# lower - Changes the case of a string to lowercase

print("AN ALL CAPS SENTENCE".lower())

# upper - Changes the case of a string to UPPERCASE

print("This is a sentence.".upper())

################################################################################

# Practice 19 - Shouting Text

# Your friend is sending you a text message, however his caps lock is broken and the whole message is in uppercase.
# Nobody likes being shouted at, plus uppercase text is hard to read, so you decide to write a program to convert the text to lowercase and output it.
# Take a string as input and output it in lowercase.

################################################################################

# Solution:

text = input(str())
print(text.lower())