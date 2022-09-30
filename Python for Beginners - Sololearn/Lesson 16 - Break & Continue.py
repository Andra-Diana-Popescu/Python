################################################################################
#####                                                                       ####
#####                       Lesson 16 - Break & Continue                    ####
#####                                                                       ####
################################################################################


# break

# Example 1:

i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")

# Example 2:

i = 5
while True:
    print(i)
    i = i - 1
    if i <= 2:
        break

# continue

# Example:

i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping 3")
        continue
    print(i)

################################################################################

# Practice 12 - Ticket Prices 

# You are making a ticketing system. The price of a single ticket is $100.
# For children under 3 years old, the ticket is free.

# Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.

# Sample Input
# 18
# 24
# 2
# 5
# 42

# Sample Output 
# 400
################################################################################

# Solution:

total = 0
passenger = 0
while passenger < 5:
   age = int(input())
   passenger += 1
   if age <= 3:
      continue 
   elif age > 3:
      ticket = 100
      total  += ticket
print(total)