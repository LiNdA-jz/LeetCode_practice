class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # not work
        # i, neq_count = 0, len(nums)
        # while i <= neq_count:
        #     if (nums[i] == val):
        #         nums.append(val)
        #         nums.pop(i)
        #         print(nums)
        #         neq_count -= 1
        #         # i -= 1

        #     i += 1

        # return neq_count

        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            nums[k] = nums[i]
            k += 1
        return k