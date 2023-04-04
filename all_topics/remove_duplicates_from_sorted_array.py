class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # not work
        # nums_unique = []
        # k = len(nums)
        # for i in nums:
        #     if i in nums_unique:
        #         k -= 1
        #     else:
        #         nums_unique.append(i)
        # nums = nums_unique
        # return k
        i, j = 0, 1
        while i<=j and j<len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
        return i+1