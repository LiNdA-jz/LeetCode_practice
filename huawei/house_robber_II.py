class Solution:
    def rob(self, nums: List[int]) -> int:
        # not work
        # if len(nums) == 1:
        #     return nums[0]
        # total_money = 0
        # total_money_odd_1, total_money_odd_2, total_money_even_1, total_money_even_2 = 0, 0, 0, 0

        # if len(nums) % 2 == 1:
        #     total_money_odd_1 = self.rob(nums[1:])
        #     total_money_odd_2 = self.rob(nums[:-1])

        #     total_money = max(total_money_odd_1, total_money_odd_2)
        # else:
        #     for i in range(0, len(nums), 2):
        #         total_money_even_1 += nums[i]

        #     for i in range(1, len(nums), 2):
        #         total_money_even_2 += nums[i]

        #     total_money = max(total_money_even_1, total_money_even_2)

        # return total_money

        def robRange(start: int, end: int) -> int:
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                # first + nums[i] not guaranteed to be greater than second!!!!!!!!
                first, second = second, max(first + nums[i], second)
            return second

        length = len(nums)
        if length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0], nums[1])
        else:
            return max(robRange(0, length - 2), robRange(1, length - 1))

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/house-robber-ii/solution/da-jia-jie-she-ii-by-leetcode-solution-bwja/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。