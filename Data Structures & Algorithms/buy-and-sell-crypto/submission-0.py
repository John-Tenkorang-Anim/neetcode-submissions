class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n):
            for j in range(i+1,n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit

        # i = 0
        # j = i + 1
        # max_profit = 0
        # while j < len(prices):
        #     if prices[j] <= prices[i]:
        #         i = j
        #         j += 1
        #     elif prices[j] > prices[i]:
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)
        #         i += 1
        #         j += 1
        #     else:
        #         return 0
        # return max_profit

        