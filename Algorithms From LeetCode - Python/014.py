# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.

import math
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         idx = 1
#         arrSqrt = []
#         arrSqrt2 = []
#         result = 1
#         if x == 0:
#             return 0
#         while x != 1:
#             idx += 1
#             if x // idx == x / idx:
#                 arrSqrt.append(idx)
#                 x = x // idx 
#                 idx -= 1
#         idx = 0
#         for i in range(len(arrSqrt)):
#             idx -= 1
#             if arrSqrt.count(arrSqrt[idx]) % 2 == 1:
#                 arrSqrt2.append(arrSqrt[idx])
#                 arrSqrt.pop(idx)
#                 idx += 1
#         for i in range(len(arrSqrt)):
#             if i % 2 == 0:
#                 result *= arrSqrt[i]
#         for i in arrSqrt2:
#             result *= math.sqrt(i)
#         result = int(result)
#         return result      
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))