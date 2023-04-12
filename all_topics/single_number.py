from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return nums[0]

        # unique_num = []

        # for i in nums:
        #     if i in unique_num:
        #         unique_num.remove(i)
        #     else:
        #         unique_num.append(i)

        # return unique_num[0]

        # if you XOR same numbers it will return zero.
        # Since the nums contains just one non-repeating number,
        # we can just XOR all numbers together
        # and the final result will be our answer
        return reduce(lambda total, el: total ^ el, nums)