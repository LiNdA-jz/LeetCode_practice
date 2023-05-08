class Solution:
    def rob(self, nums: List[int]) -> int:
        # forgot the logic from bobber II......
        # if len(nums) <= 2:
        #     return max(nums)

        # first = nums[0]
        # second = nums[2]
        # max_money = 0

        # for i in range(1, len(nums)):
        #     first = max(first, nums[i])
        #     second = max()

        # return max_money

        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)

        return second

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/house-robber/solution/da-jia-jie-she-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。