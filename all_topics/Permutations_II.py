class Solution:
    # low performance for memory
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums]
            else:
                return [nums, nums[::-1]]

        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if i < len(nums) - 1:
                next_perm = self.permuteUnique(nums[i+1:] + nums[:i])
            else:
                next_perm = self.permuteUnique(nums[::-1][1:])
            for perm in next_perm:
                # print(perm)
                res.append([nums[i]] + perm)

        return res

    # 搜索回溯
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, ans, idx, perm):
            if idx == len(nums):
                # perm -> 前拷贝 -> not work
                ans.append(perm[::])
                return

            for i in range(len(nums)):
                if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                    continue

                perm.append(nums[i])
                visited[i] = 1
                backtrack(nums, ans, idx + 1, perm)
                visited[i] = 0
                perm.pop()

        ans = []
        perm = []
        visited = [0] * len(nums)
        nums.sort()
        backtrack(nums, ans, 0, perm)

        return ans