################################################################################
#####                                                                       ####
#####                         Lesson 19 - List Slices                       ####
#####                                                                       ####
################################################################################


# Example 1:

# This will return a new list containing all the values in the old list between indices

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

# Example 2:

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sqs[4:7])

# Example 3:

# If the first number in a slice is omitted, it's taken to be the start of the list 
# If the second number in a slice is omitted, it's taken to be the end of the list 

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

# Example 4:

list = ["a", "b", "c", "d"]
a = list[0:2]
print(a)

# Example 5:

# Just like with ranges, your list slices can include a third number, representing the step, to include only alternate values in the slice

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])
print(squares[2::3])
print(squares[4::])

# Example 6:

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

# Example 7:

# Negative values can also be used in list slicing

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])

# Example 8:

# list[-1::] ---> list only the last element 
# list[:-1:] ---> all list except the last element 
# list[-1::] ---> list in backwards order

list = [1, 2, 3, 4, 5]
print(list[-1::])
print(list[:-1:])
print(list[::-1])

# Example 9:

# You can reverse a string or a list using index slicing

string = "Hello"
rev_str = string[::-1]
print(rev_str)

# Example 10:

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

# Look: start 7 is 49
#       stop 5 is 25
#       step -1 is reversed
# So, [start:stop:step] is [7:5:-1] => [49,36]

################################################################################

# Practice 16 - Flip a String

# Reversing a string is a common task during coding interviews.
# Given a string as input, output its reverse.

# Sample Input
# hello world

# Sample Output 
# dlrow olleh

################################################################################

# Solution:

words = input()
print(words[::-1])

################################################################################

# Practice 17 - Sum of Consecutive Numbers

# Take a number N as input and output the sum of all numbers from 1 to N (including N).

# Sample Input 
# 100

# Sample Output 
# 5050

# Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
# You can iterate over a range and calculate the sum of all numbers in the range.
# Remember, range(a, b) does not include b, thus you need to use b+1 to include b in the range.

################################################################################

# Solution:

N = int(input())

sum = int((N * (N + 1)) / 2)
print(sum)