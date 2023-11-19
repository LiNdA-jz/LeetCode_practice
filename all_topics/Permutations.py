class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]

        elif len(nums) == 2:
            return [nums[:], nums[::-1]]

        else:
            res = []
            for i in range(len(nums)):
                start = nums[i]
                next_perm = self.permute(nums[i+1:] + nums[:i])
                for perm in next_perm:
                    res.append([start] + perm)

            return res

    # 1, 2, 3
    # first = 0
    # 123, 213, 321
    # first = 1
    # 123, 132, 213, 231, 321, 312
    # first = 2 = n -> append
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/permutations/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。