class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def findCurMin(ls):
            left, right = 0, len(ls) - 1

            if len(ls) == 1:
                return ls[0]

            if ls[left] < ls[right]:
                return ls[left]

            else:
                mid = (right - left) // 2 + 1
                return min(findCurMin(ls[left:mid]), findCurMin(ls[mid:]))

        return findCurMin(nums)

    # 二分查找
    # 左边界为 low，右边界为 high，区间的中点为 pivot
    # 将中轴元素 nums[pivot] 与右边界元素 nums[high] 进行比较，可能会有以下的三种情况
    # nums[pivot]<nums[high] -> 说明 nums[pivot] 是最小值右侧的元素，因此我们可以忽略二分查找区间的右半部分
    # nums[pivot]>nums[high] -> nums[pivot] 是最小值左侧的元素，因此我们可以忽略二分查找区间的左半部分
    # 只要当前的区间长度不为 1，pivot 就不会与 high 重合
    # 如果当前的区间长度为 1，这说明我们已经可以结束二分查找了
    # 不会存在 nums[pivot]=nums[high]
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            else:
                low = pivot + 1
        return nums[low]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/solutions/698479/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。