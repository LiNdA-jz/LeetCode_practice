class Solution:
    # low performance (time & memory)
    def search(self, nums: List[int], target: int) -> int:
        nums_last = nums[-1]
        nums_first = nums[0]

        if target == nums_first:
            return 0
        elif target == nums_last:
            return len(nums) - 1
        elif len(nums) <= 1:
            return 0 if target == nums[0] else -1
        else:
            l, r = 0, len(nums) - 1
            if target > nums_first:
                while target > nums[l] and l < r:
                    l += 1
                return l if target == nums[l] else -1
            else:
                while target < nums[r] and r > l:
                    r -= 1
                return r if target == nums[r] else -1

    # 二分查找
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/search-in-rotated-sorted-array/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。