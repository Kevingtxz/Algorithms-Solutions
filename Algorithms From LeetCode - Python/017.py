# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        elif rowIndex < 0:
            return [-1]
        result = [[1, 1]]
        for i in range(rowIndex-1):
            result.append([])
            for j in range(i+1):
                if j == 0:
                    result[i+1].append(1 + result[i][j])
                elif j >= len(result[i]):
                    result[i+1].append(result[i][j-1]+1)
                else:
                    result[i+1].append(result[i][j-1]+result[i][j])
        result[-1].insert(0, 1)
        result[-1].append(1)
        return result[-1]