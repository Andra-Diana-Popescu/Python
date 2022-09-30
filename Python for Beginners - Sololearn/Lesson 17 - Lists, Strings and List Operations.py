################################################################################
#####                                                                       ####
#####            Lesson 17 - Lists, Strings and List Operations             ####
#####                                                                       ####
################################################################################


# Lists

# Example 1:

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])

# Example 2:

nums = [5, 4, 3, 2, 1]
print(nums[1])

# Example 3:

m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
print(m[1][2])

# Example 4:

list = [42, 55, 67]
print(list[2])

# Strings

# Example 1:

str = "Hello world!"
print(str[6])

# Example 2:

x = "Python"
print(x[1] + x[4])

# List Operations

# Example 1:

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

# Example 2:

x = [2, 4]
x += [6, 8]
print(x[2] // x[0])

# Example 3:

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

# Example 4:

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5

if 4 in nums:
    print(nums[3])
else:
    print(nums[4])

# Example 5:

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

# Example 6:

letters = ['a', 'b', 'z']
if "z" in letters:
    print("Yes")

################################################################################

# Practice 13 - Voice Recognition System

# You're making a voice recognition system. The supported commands are stored in a list.
# Complete the program to take a command as input, check if it's supported and output "OK" if it is, and "Not supported", if not.

# Sample Input
# Lights Off

# Sample Output
# OK
################################################################################

# Solution:

commands = ["Lights Off", "Lock the door", "Open the door", "Make Coffee", "Shut down"]

voice = input()

if voice in commands:
	print ("OK")
else:
	print ("Not supported")