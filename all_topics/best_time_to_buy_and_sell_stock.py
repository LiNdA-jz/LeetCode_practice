class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Limit Exceeded
        # p_len = len(prices)

        # max_profit = 0
        # for i in range(p_len - 1):
        #     cur_p = prices[i]
        #     cur_max = max(prices[i+1:])
        #     # cur_max = sorted(prices[i+1:])[-1]
        #     max_profit = max(max_profit, cur_max - cur_p)

        # return max_profit

        # use pointer
        # left = 0 #Buy
        # right = 1 #Sell
        # max_profit = 0
        # while right < len(prices):
        #     currentProfit = prices[right] - prices[left] #our current Profit
        #     if prices[left] < prices[right]:
        #         max_profit = max(currentProfit,max_profit)
        #     else:
        #         left = right
        #     right += 1
        # return max_profit

        # one pass
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit