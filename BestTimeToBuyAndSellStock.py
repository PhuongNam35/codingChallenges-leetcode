    #You are given an array prices where prices[i] is the price of a given stock on the ith day.
    #You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock.
    #Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.

from typing import List

#Using this function causes a Time limit Exceeded error (due to 2 for loops)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices), 1):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]
        return max_profit

    def maxProfit_2(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right
            right += 1
        return max_profit


ans = Solution()
result = ans.maxProfit_2([7,1,5,3,6,4])
print(result)