from re import search


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # not work
        if (len(nums)%2==1):
            nums_idx = (len(nums)+1) // 2
        else:
            nums_idx = int(len(nums) / 2)

        pt_l = 0
        pt_r = len(nums) - 1
        
        
        while (nums_idx>1):
            if (target==nums[nums_idx]):
                return nums_iidx
            elif (target<nums[nums_idx]):
                pt_r = nums_idx
            else:
                pt_l = nums_idx
            search(nums[pt_l:pt_r], target)
            nums_idx //= 2
                

        return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1