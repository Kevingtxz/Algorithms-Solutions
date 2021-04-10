class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        val, result = grid[0][0], 0
        for i1 in range(len(grid)):
            val2 = max(grid[i1])
            for i2 in range(len(grid[0])):
                old = grid[i1][i2]
                for i3 in range(len(grid)):
                    if grid[i3][i2] > val:
                        val = grid[i3][i2]
                if val < val2:
                    grid[i1][i2] = val
                else:
                    grid[i1][i2] = val2
                result += grid[i1][i2] - old
                val = 0
        return result