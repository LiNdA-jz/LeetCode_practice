class Solution:
    # need backtrace?
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     print(s, wordDict)
    #     if s in wordDict:
    #         return True
    #     i = 0
    #     while i <= len(s):
    #         if s[:i] in wordDict:
    #             if i == len(s):
    #                 return True
    #             else:
    #                 return self.wordBreak(s[i:], wordDict)
    #         i += 1

    #     return False

    # 动态规划
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]