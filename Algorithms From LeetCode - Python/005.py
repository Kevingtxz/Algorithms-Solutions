# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        v = 2**31
        if -v <= x <= v-1:
            isNegative = False
            if x < 0:
                isNegative = True
                x *= -1
            newX = str(x)[::-1]
            i = 0
            while True:
                if(newX[0] != '0'):
                    break
                newX = newX[1::]
            if isNegative:
                return '-' + newX
            return newX
        else:
            return 0
        