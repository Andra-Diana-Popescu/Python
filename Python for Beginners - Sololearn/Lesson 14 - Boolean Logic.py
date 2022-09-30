################################################################################
#####                                                                       ####
#####                        Lesson 14 - Boolean Logic                      ####
#####                                                                       ####
################################################################################


# Operators: and, or, not

# and

print( 1 == 1 and 2 == 2)
print( 1 == 1 and 2 == 3)
print( 1 != 1 and 2 == 2)
print( 2 < 1 and 3 > 6)

# Example:

if (1 == 1) and (2 + 2 > 3):
    print("true")
else:
    print("false")

# or

print( 1 == 1 or 2 == 2)
print( 1 == 1 or 2 == 3)
print( 1 != 1 or 2 == 2)
print( 2 < 1 or 3 > 6)

# Example:

age = 15
money = 500

if age > 18 or money > 100:
    print("Welcome")

# not

print(not 1 == 1)
print(not 1 > 7)

# Example:

if not True:
    print("1")
elif not (1 + 1 == 3):
    print("2")
else:
    print("3")