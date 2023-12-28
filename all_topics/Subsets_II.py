class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        if n == 1:
            return [[], nums]

        if len(set(nums)) == 1:
            # print([[nums[0]] * i for i in range(n + 1)])
            return [[nums[0]] * i for i in range(n + 1)]

        res = [[]]
        for i in range(1, n + 1):
            sub_subset = self.subsetsWithDup(nums[i:])
            print(sub_subset)
            for j in sub_subset:
                if [nums[i - 1]] + j not in res:
                    res.append([nums[i - 1]] + j)

        return res

    # 迭代
    # 对于当前选择的数 x，若前面有与其相同的数 y，且没有选择 y，此时包含 x 的子集，必然会出现在包含 y 的所有子集中
    # 先将数组排序；迭代时，若发现没有选择上一个数，且当前数字与上一个数相同，则可以跳过当前生成的子集
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        t, ans = [], []

        nums.sort()
        n = len(nums)

        for mask in range(1 << n):
            t = []
            flag = True

            for i in range(n):
                if (mask & (1 << i)):
                    if (i > 0 and (mask >> (i - 1) & 1) == 0 and nums[i] == nums[i - 1]):
                        flag = False
                        break
                    t.append(nums[i])

            if flag:
                ans.append(t)

        return ans

    # 递归
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        t, ans = [], []

        def dfs(choosePre, cur, nums):
            if (cur == len(nums)):
                ans.append(t[:])
                return

            dfs(False, cur + 1, nums[:])

            if (not choosePre and cur > 0 and nums[cur - 1] == nums[cur]):
                return

            t.append(nums[cur])

            dfs(True, cur + 1, nums[:])

            t.pop()

        nums.sort()
        dfs(False, 0, nums[:])

        return ans