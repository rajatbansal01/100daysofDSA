# A child is playing a cloud hopping game. In this game, there are sequentially numbered clouds that can be thunderheads or cumulus clouds. The character must jump from cloud to cloud until it reaches the start again.

# There is an array of clouds, e and an energy level e=100. The character starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[(i+k)%n]. If it lands on a thundercloud, c[i]=1, its energy (e) decreases by 2 additional units. The game ends when the character lands back on cloud 0.

# Given the values of n, k, and the configuration of the clouds as an array c, determine the final value of e after the game ends.

# Example. c = [0,0,1,0] and k=2, then the character makes the following jumps:

# The indices of the path are 0 -> 2 -> 0 . The energy level reduces by 1 for each jump to 98. The character landed on one thunderhead at an additional cost of 2 energy units. The final energy level is 96.

def jumpingOnClouds(c, k):
    # There is an array of clouds, e and an energy level e=100. The character starts from c[0] and uses 1 unit of energy to make a jump of size k to cloud c[(i+k)%n]. If it lands on a thundercloud, c[i]=1, its energy (e) decreases by 2 additional units. The game ends when the character lands back on cloud 0.
    # The indices of the path are 0 -> 2 -> 0 . The energy level reduces by 1 for each jump to 98. The character landed on one thunderhead at an additional cost of 2 energy units. The final energy level is 96.
    e = 100
    i = 0
    while i != 0:
        if c[(i+k)%len(c)] == 1:
            e -= 2
        e -= 1
        i = (i+k)%len(c)
    return e


    