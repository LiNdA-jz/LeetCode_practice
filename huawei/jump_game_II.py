class Solution:
    def jump(self, nums: List[int]) -> int:
        # not work
        # if len(nums) == 1:
        #     return 0
        # min_jump = len(nums)

        # dp = [min_jump] * min_jump
        # dp[0] = 0
        # # print(dp)
        # for i in range(len(nums)):
        #     for k in range(1, nums[i]+1):
        #         if i + k >= len(nums) - 1:
        #             min_jump = min(min_jump, dp[i]+1)
        #         else:
        #             dp[i+k] = dp[i] + 1

        # return min_jump

        ans, end, maxPos = 0, 0, 0

        for i in range(len(nums)-1):
            maxPos = max(nums[i] + i, maxPos)

            if i == end:
                end = maxPos
                ans += 1
        return ans

    # 作者：ikaruga
    # 链接：https://leetcode.cn/problems/jump-game-ii/solution/45-by-ikaruga/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。