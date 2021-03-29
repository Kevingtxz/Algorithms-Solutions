# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commom = ''
        if len(strs) > 0:
            end = False
            for i in range(len(min(strs))):
                for i2 in range(len(strs)):
                    if strs[0][i] != strs[i2][i]:
                        return commom
                commom += strs[0][i]
        return commom