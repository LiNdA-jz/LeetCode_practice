class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        if len(nums) == 1:
            res.append(nums)
            return res

        for i in range(len(nums)):
            sub_sub = self.subsets(nums[1:])
            for j in sub_sub:
                res.append([nums[0]] + j)

            nums = nums[1:]

        return res

    # 迭代
    # 位运算
    # 0/1序列	子集	    0/1序列对应的二进制数
    # 000	    {}	        0
    # 001	    {9}	        1
    # 010	    {2}	        2
    # 011	    {2,9}	    3
    # 100	    {5}	        4
    # 101	    {5,9}	    5
    # 110	    {5,2}	    6
    # 111	    {5,2,9}	    7

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/subsets/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        n = len(nums)

        for mask in range(1 << n):
            t = []

            for i in range(n):
                if mask & (1 << i):
                    t.append(nums[i])

            ans.append(t)

        return ans

    # 递归
    def subsets(self, nums: List[int]) -> List[List[int]]:
        t = []
        ans = []

        def dfs(cur, nums):
            if cur == len(nums):
                ans.append(t[:])
                return
            t.append(nums[cur])
            dfs(cur + 1, nums)
            t.pop()

            dfs(cur + 1, nums)

        dfs(0, nums)

        return ans