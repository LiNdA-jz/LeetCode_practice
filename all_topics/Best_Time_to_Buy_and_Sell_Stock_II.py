class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        # remove cum. 0
        def remove_zero(prices):
            for i in range(n):
                if prices[i] == 0 and prices[i:] == [0] * (n - i):
                    return prices[:i]
            return prices[:]

        prices = remove_zero(prices)
        n = len(prices)

        # dp
        max_sum = [0] * n
        for i in range(n):
            max_sum[i] = max(max_sum[i], prices[i] - prices[0])

        for i in range(1, n - 1):
            for j in range(i + 1, n):
                max_sum[j] = max_sum[j - 1] + max(prices[j] - prices[i], 0)

        # print(max_sum)
        return max_sum[-1]

    # 动态规划
    # dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润，dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润
    # dp[i][0]=max{dp[i−1][0],dp[i−1][1]+prices[i]}
    # dp[i][1]=max{dp[i−1][1],dp[i−1][0]−prices[i]}
    # dp[0][0]=0，dp[0][1]=−prices[0]
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [[0] * 2 for _ in range(n)]

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n - 1][0]

    # 每一天的状态只与前一天的状态有关
    # 将 dp[i−1][0] 和 dp[i−1][1] 存放在两个变量中
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp_0, dp_1 = 0, -prices[0]

        for i in range(1, n):
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, dp_0 - prices[i])

        return dp_0

    # 贪心
    # 整个问题等价于寻找 x 个不相交的区间 (li,ri] 使得如下的等式最大化
    # a[ri] - a[li] = (a[ri] - a[ri - 1]) + (a[ri - 1] - a[ri - 2]) + ... + (a[li + 1] - a[li])
    # ans = sum_{i = 1}^{n - 1} max(0, a[i] - a[i - 1])
    # 只能用于计算最大利润，计算的过程并不是实际的交易过程
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)

        for i in range(1, n):
            ans += max(0, prices[i] - prices[i - 1])

        return ans

    # 因为交易次数不受限，如果可以把所有的上坡全部收集到，一定是利益最大化的
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        ans = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                ans += prices[i] - prices[i - 1]

        return ans