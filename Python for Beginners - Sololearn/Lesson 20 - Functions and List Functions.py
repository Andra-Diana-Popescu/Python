################################################################################
#####                                                                       ####
#####                Lesson 20 - Functions and List Functions               ####
#####                                                                       ####
################################################################################


# Examples of functions:

# print("Hello world!")
# range(2, 20)
# str(12)
# range(10, 20, 3)

# Example 1:

# len() - You get the number of items in a list

nums = [1, 3, 5, 2, 4]
print(len(nums))

# len() starts counting from 1

# Example 2:

letters = ["a", "b", "c"]
letters += ["d"]
print(len(letters))

# Python List Methods

# list.append() - Adds an element at the end of the list

nums = [1, 2, 3]
nums.append(4)
print(nums)

# list.insert() - Adds an element at the specified position

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

# list.index() - Returns the index of the first element with the specified value

letters = ['p', 'q', 'r', 's', 'p', 'u']

print(letters.index('r'))
print(letters.index('p'))
print(letters.index('q'))

# index() starts counting from 0

# max(list) - Returns the maximum value

lotto = [1, 5, 49, 6, 22, 34, 8]

print(max(lotto))

# min(list) - Returns the minimum value

print(min(lotto))

# list.count(item) - Returns a count of how many times an item occurs in a list

print(lotto.count(22))

# list.remove(item) - Removes the first item from a list with the specified value

print(lotto.remove(22))
print(lotto)

# list.reverse() - Reverses items in a list

print(lotto.reverse())
print(lotto)

# list.copy() - Returns a copy of the list

print(lotto.copy())

# list.extend() - Add the elements of a list (or any iterable) to the end of the current list (list ot tuple or string)

print(lotto.extend("dodo"))
print(lotto)

# list.pop() - Removes the element at the specified position

print(lotto.pop(0))
print(lotto)

# remove() - I repeated this because I want to use the sort()

print(lotto.remove('d'))
print(lotto.remove('o'))
print(lotto.remove('d'))
print(lotto.remove('o'))
print(lotto)

# list.sort() - Sorts the list

print(lotto.sort())
print(lotto)

# list.clear() - Removes all the elements from the list

print(lotto.clear())
print(lotto)

################################################################################

# Practice 18 - Analyze to Realize

# You’re analyzing a data set and need to remove the outliers (the smallest and largest values). The data is stored in a list. 
# Remove the smallest and largest elements from the list and output the sum of the remaining numbers.

# data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1024, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]

################################################################################

# Solution:

data = [7, 5, 6.9, 1, 8, 42, 33, 128, 1024, 2, 8, 11, 0.4, 1025, 66, 809, 11, 8.9, 1.1, 3.42, 9, 100, 444, 78]

data.remove(max(data))
data.remove(min(data))

print(sum(data))