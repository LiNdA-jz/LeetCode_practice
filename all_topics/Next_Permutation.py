class Solution:
    # low performance (time & memory)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            nums = nums

        elif nums[-1] <= nums[-2]:
            nums_copy = nums
            nums_sorted = sorted(nums_copy)
            # print(nums, nums_copy, nums_sorted)
            sub_nums_sorted = sorted(nums[1:])
            # print(nums_sorted, nums[::-1])
            # print(sub_nums_sorted[::-1], nums[1:])
            if nums[::-1] == nums_sorted:
                # print("MAX")
                nums.sort()
                # print(nums)
            elif sub_nums_sorted[::-1] == nums[1:]:
                # print("MAX for nums[1:]")
                cur_i = -1
                for i in range(len(nums)):
                    if nums_sorted[i] == nums[0]:
                        temp = nums[:-1]
                        i += 1
                        while nums_sorted[i] == nums_sorted[i-1] and i < len(nums):
                            i += 1
                        nums[0] = nums_sorted[i]
                        nums[1:] = nums_sorted[:i] + nums_sorted[i+1:]
                        # cur_i = i
                        # print(nums, cur_i)
                        break
                # print(nums, cur_i)
            else:
                # print("ELSE")
                sub_nums = nums[1:]
                # print(sub_nums)
                self.nextPermutation(sub_nums)
                nums[1:] = sub_nums
                # print(nums)

        else:
            temp = nums[-1]
            nums[-1] = nums[-2]
            nums[-2] = temp
            # print(nums)

    """
    标准的 “下一个排列” 算法可以描述为：

        1. 从后向前 查找第一个 相邻升序 的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
        2. 在 [j,end) 从后向前 查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」
        3. 将 A[i] 与 A[k] 交换
        4. 可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
        5. 如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4

        该方法支持数据重复，且在 C++ STL 中被采用。

        作者：Imageslr
        链接：https://leetcode.cn/problems/next-permutation/
        来源：力扣（LeetCode）
        著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return

        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

        # find A[i] < A[j]
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        # not last perm.
        if i >= 0:
            # find A[i] < A[k]
            while nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
            # print(nums[i+1:])
            nums[i+1:] = nums[i+1:][::-1]
            # print(nums[i+1:])

        # reverse A[j:end]
        else:
            nums.sort()