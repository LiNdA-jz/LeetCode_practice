class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while (left<=right):
            pivot = left + (right - left)//2

            if (nums[pivot]==target):
                return pivot
            elif(target<nums[pivot]):
                right -= 1
            else:
                left += 1
        

        return left