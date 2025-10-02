def maxProfit(prices: list[int]) -> int:
    # O(n) / O(1)
    maxProfit = 0
    maxPrice = prices[-1]
    for buyDay in range(len(prices) - 2, -1, -1):
        currMaxProfit = maxPrice - prices[buyDay]
        maxProfit = max(maxProfit, currMaxProfit)
        maxPrice = max(maxPrice, prices[buyDay])
    return maxProfit


print(maxProfit([7, 1, 5, 3, 6, 4]))
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Input: [7, 6, 4, 3, 1]
# Output: 0
# Usage: Find maximum profit from a single buy/sell in stock prices
# Useful for: array analysis, greedy problems, financial algorithms
