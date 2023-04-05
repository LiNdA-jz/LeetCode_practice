class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # i, j = 0, len(nums)
        # while (i<=j and i<= len(nums) - 1):
        #     if (nums[i] == target):
        #         return i
        #     elif (nums[i] < target):
        #         i += 1
        #     else:
        #         j -= 1
        # return j if (i<=j) else i

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        return left 