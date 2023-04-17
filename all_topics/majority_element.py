class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # max_count = len(nums) // 2
        # if (len(nums) == 1):
        #     return nums[0]

        # nums = sorted(nums)
        # cur_count = 0

        # for i in range(1, len(nums)):
        #     if nums[i-1] == nums[i]:
        #         cur_count += 1
        #         if cur_count == max_count:
        #             return nums[i-1]
        #     else:
        #         cur_count = 0

        x = len(nums)
        n = len(nums) // 2
        while x != 0:
            if (nums.count(nums[x - 1]) > n):
                return nums[x - 1]
            else:
                x -= 1