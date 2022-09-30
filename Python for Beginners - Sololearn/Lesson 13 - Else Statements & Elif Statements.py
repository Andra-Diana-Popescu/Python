################################################################################
#####                                                                       ####
#####              Lesson 13 - Else Statements & Elif Statements            ####
#####                                                                       ####
################################################################################


# else

# Example 1:

x = 4
if x == 5:
    print("Yes")
else:
    print("No")

# Example 2:

if 1 + 1 == 2:
    if 2 * 2 == 8:
        print("if")
    else:
        print("else")

# Example 3:

num = 3
if num == 1:
    print("One")
else:
    if num == 2:
        print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("Something else")

# Example 4:

x = 10
y = 20

if x > y:
    print("if statement")
else:
    print("else statement")

# elif

# The same example from the previous part can be rewritten using elif statements:

num = 3
if num == 1:
    print("One")
elif num == 2:
        print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")

################################################################################

# Practice 10 - BMI Calculator

# Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight.
# It’s calculated using a person's weight and height, using this formula: weight / height²
# The resulting number indicates one of the following categories:

# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more

# Let’s make finding out your BMI quicker and easier, 
# by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

# Sample Input
# 85
# 1.9

# Sample Output
# Normal

################################################################################

# Solution:

weight=float(input())
height=float(input())

bmi= weight/(height)**2

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obesity")