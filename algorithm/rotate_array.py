class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # don't know why stdout != output
        n = len(nums)
        cut_list = nums.copy()[-k:]
        for i in cut_list:
            nums.remove(i)
        
        cut_list.extend(nums)
        # print(cut_list, nums)
        nums = cut_list
        print(nums)

        n = len(nums)
        # required for k>n
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]