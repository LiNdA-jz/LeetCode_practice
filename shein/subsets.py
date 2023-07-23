class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) == 1:
        #     return [nums]

        # return [[], nums] + self.subsets(nums[0:-1]) + self.subsets(nums[1:])

        # res = []
        # for i in range(len(nums)+1):
        #     for tmp in itertools.combinations(nums, i):
        #         res.append(tmp)
        # return res

        # 作者：powcai
        # 链接：https://leetcode.cn/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

# 作者：powcai
# 链接：https://leetcode.cn/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# res = []
# n = len(nums)

# def helper(i, tmp):
#     res.append(tmp)
#     for j in range(i, n):
#         helper(j + 1,tmp + [nums[j]] )
# helper(0, [])
# return res

# 作者：powcai
# 链接：https://leetcode.cn/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。