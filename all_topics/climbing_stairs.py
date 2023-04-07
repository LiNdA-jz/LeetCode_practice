class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # not work
        # tot_count = 0
        # if n%2 == 1:
        #     return int(n*(n-1)/2) + 1
        # else:
        #     i = n - 1
        #     while i>1:
        #         tot_count += i
        #         i -= 1
        #     return tot_count + 2


        # one, two=1, 1
        # for i in range(n-1):
        #     temp = one + two
        #     one = two
        #     two = temp
        # return two

        # Intuition : the next distinct way of climbing stairs is equal to the sum of the last two distinct way of climbing
        # distinct(n) = distinct(n-1) + distinct(n-2)
        # edge cases
        if n==0: return 0
        if n==1: return 1
        if n==2: return 2
        dp = [0] * (n+1) # considering zero steps we need n+1 places
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[n]