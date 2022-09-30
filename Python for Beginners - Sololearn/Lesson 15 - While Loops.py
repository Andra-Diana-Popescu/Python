################################################################################
#####                                                                       ####
#####                        Lesson 15 - While Loops                        ####
#####                                                                       ####
################################################################################


# Example 1:

i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Finished!")

# Example 2:

i = 3
while i >= 0:
    print(i)
    i = i - 1

# Example 3:

x = 1
while x < 10:
    if x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")

    x += 1

# Example 4:

x = 0
while x <= 20:
    print(x)
    x += 2

################################################################################

# Practice 11 

# You are making a game! The player tries to shoot an object and can hit or miss it.
# The player starts with 100 points, with a hit adding 10 points to the player’s score, and a miss deducting 20 points.
# Your program needs to take 4 action results as input ("hit" or "miss"), calculate and output the player’s remaining points.

# Sample Input
# hit
# hit
# miss
# hit

# Sample Output
# 110

# Explanation: 3 hits add 30 points, one miss deducts 20, making the total points equal to 110
################################################################################

# Solution:

points = 100
i = 1
while i <= 4:
    x = input()
    if x == "hit":
        points +=10
    elif x == "miss":
        points -=20
    i = i+1
print(points)