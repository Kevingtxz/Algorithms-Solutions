# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        if digits.count(9) == len(digits):
            res = [1]
            for i in range(len(digits)):
                res.append(0)
            return res
        digits.reverse()
        for i in range(len(digits)):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        digits.reverse()
        return digits