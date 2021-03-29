# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

# Note:

# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# Example:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if target == 0:
            return [1,2]
        arr = ['x']
        if 0 in numbers:
            arr.insert(0, 0)
            arr.append(0)
        if target < 0:
            for i in numbers:
                if i >= 0:
                    break
                if i >= target and i <= target/2:
                    arr.insert(0,i)
                elif i >= target:
                    arr.append(i)
        else:
            for i in numbers:
                if i <= target and i >= target/2:
                    arr.append(i)
                elif i <= target:
                    arr.insert(0, i)
        for i in range(len(arr)-arr.index('x')-1):
            for j in range(arr.index('x')):
                if arr[j] + arr[-i-1] == target:
                    return [numbers.index(arr[j])+1, numbers.index(arr[-i-1])+1]
        if arr.count(arr[-1]) > 1:
            return [numbers.index(arr[-1])+1,numbers.index(arr[-1])+2]