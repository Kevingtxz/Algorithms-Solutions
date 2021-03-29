# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub = -1
        i = 0
        letters =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','y','x','z','0','1','2','3','4','5','6','7','8','9']
        print(len(s))
        while i <= len(s)-1:
            if s[i].lower() not in letters:
                i += 1
                continue
            elif s[sub].lower() not in letters:
                sub -= 1
                continue
            elif s[i].lower() == s[sub].lower():
                i += 1
                sub -= 1
                continue
            else:
                return False
        return True