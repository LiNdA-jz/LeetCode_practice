from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute-force
        # for i in range(len(nums)):
        #     second = target - nums[i]
        #     if second in nums:
        #         second_idx = nums.index(second)
        #         if second_idx != i:
        #             return [i, second_idx]
        
        # hash map
        complementMap = dict()
        
        for i in range(len(nums)):
            first = nums[i]
            complement = target - first
            if first in complementMap:
                return [complementMap[first], i]
            else:
                complementMap[complement] = i