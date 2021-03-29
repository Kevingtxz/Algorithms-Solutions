# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        arrResult = []
        max = prices[0]
        min = prices[0]
        dateMin = 0
        dateMax = 0
        i = 0
        while i < len(prices)-1:
            i += 1
            if min > prices[i]:
                if i > dateMax:
                    arrResult.append(max-min)
                    max = 0
                    dateMax = 0
                min = prices[i]
                dateMin = i
            elif prices[i] > max and i > dateMin:
                max = prices[i]
                dateMax = i
        arrResult.append(max-min)
        arrResult.sort()
        return arrResult[-1]