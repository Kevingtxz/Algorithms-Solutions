# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true
class Solution:
    def isValid(self, s: str) -> bool:
        opens = '([{'
        closes = ')]}'
        opensStr = []
        for i in range(len(s)):
            if s[i] in opens:
                opensStr.append(s[i])
            elif s[i] in closes and len(opensStr) > 0:
                if opens.find(opensStr[-1]) == closes.find(s[i]):
                    opensStr.pop(-1)
                else:
                    return False
            else: 
                return False
        if opensStr:
            return False
        return True