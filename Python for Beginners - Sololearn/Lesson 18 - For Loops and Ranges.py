################################################################################
#####                                                                       ####
#####                   Lesson 18 - For Loops and Ranges                    ####
#####                                                                       ####
################################################################################


# for

# Example 1:

words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")

# Example 2:

letters = ['a', 'b', 'c']
for l in letters:
    print(l)

# Example 3:

str = "testing for loops"
count = 0
for x in str:
    if (x == 't'):
        count += 1
    print(count)

# Example 4:

lists = [2, 3, 4, 5, 6, 7]
for x in lists:
    if(x % 2 == 1 and x > 4):
        print(x)
        break

# Ranges

# range(start, stop, step)

# Example 1: 

example1 = list(range(10))
print(example1)

# If only one argument is given, it is the 'stop' argument:
# range(stop)

# Example 2:

example2 = list(range(5))
print(example2)

# If two arguments are given:
# range(start, stop)

# Example 3:

example3 = list(range(6,10))
print(example3)

# If three arguments are given, we use the 'step' argument:
# range(start, stop, step)

# Example 4:

example4 = list(range(0, 10, 2))
print(example4)

# Guess the result of this code:

# Example 5:

nums = list(range(5))
print(nums[4])

# Example 6:

y = list(range(20, 5, -2))
print(y)

# Example 7:

a = list(range(3, 8))
print(a)

# Example 8:

print(range(20) == range(0, 20))

# Example 9:

print(list(range(5, 20, 2)))

# Example 10:

c = list(range(3, 15, 3))
print(c[2])

# for loops & range

for i in range(5):
    print("hello!")

for i in range(0, 20, 2):
    print(i)

################################################################################

# Practice 14 - Shopping Cart

# You’re making a shopping cart program. The shopping cart is declared as a list of prices, 
# and you need to add functionality to apply a discount and output the total price.
# Take the discount percentage as input, calculate and output the total price for the shopping cart.

# Use a for loop to iterate over the list. 
# Use the following formula to calculate the result of X% discount on $Y price: Y - (Y*X/100)
# cart = [15, 42, 120, 9, 5, 380]

################################################################################

# Solution:

cart = [15, 42, 120, 9, 5, 380]

discount = int(input())
total = 0
for item in cart:
	total += item - (item * discount/100)
print(total)

################################################################################

# Practice 15 - Nearest Bathroom

# A group of buildings have restrooms on every 5th floor. For example, a building with 12 floors has restrooms on the 5th and 10th floors. 
# Create a program that takes the total number of floors as input and outputs the floors that have restrooms.

# Sample Input
# 23

# Sample Output
# 5
# 10
# 15
# 20

# You can define a range with the corresponding rules and output the numbers in that range.
# Remember, that range(a, b) includes a, but does not include b.

################################################################################

# Solution:

n = int(input())
for bathroom in (range(5, n, 5)):
	print(bathroom)