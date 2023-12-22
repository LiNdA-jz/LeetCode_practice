class Solution:
    # sort & search
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 1:
            return target == nums[0]

        # sort
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                nums = nums[i:] + nums[:i]
                break

        # print(nums)

        # search
        l, r = 0, n - 1
        if target == nums[l] or target == nums[r]:
            return True

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return True
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False

    # no sort
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, n - 1

        while l <= r:
            if target == nums[l] or target == nums[r]:
                return True
            if target > nums[l]:
                l += 1
            elif target < nums[r]:
                r -= 1
            else:
                return False

        return False

    # 二分查找
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        n = len(nums)
        if n == 1:
            return nums[0] == target

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target and target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。