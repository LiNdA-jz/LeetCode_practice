class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_zero = nums.count(0)
        count_one = nums.count(1)
        count_two = nums.count(2)

        # print(count_zero, count_one, count_two)

        for i in range(len(nums)):
            if i < count_zero:
                nums[i] = 0
            elif i < count_zero + count_one:
                nums[i] = 1
            else:
                nums[i] = 2

    # 单指针
    # 在第一次遍历中，我们将数组中所有的 0 交换到数组的头部
    # 在第二次遍历中，我们将数组中所有的 1 交换到头部的 0 之后
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/sort-colors/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 双指针
    # 当 p0<p1时，我们已经将一些 1 连续地放在头部，此时一定会把一个 1 交换出去
    # 因此，如果 p0<p1，那么我们需要再将 nums[i] 与 nums[p1] 进行交换
    # 无论是否有 p0<p1，我们需要将 p0 和 p1 均向后移动一个位置

    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0 = p1 = 0
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[p1] = nums[p1], nums[i]
                p1 += 1
            elif nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                if p0 < p1:
                    nums[i], nums[p1] = nums[p1], nums[i]
                p0 += 1
                p1 += 1


# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/sort-colors/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 双指针
    # 使用指针 p0 来交换 0，p2 来交换 2。此时，p0 的初始值仍然为 0，而 p2 的初始值为 n−1
    # 找出所有的 0 交换至数组的头部，并且找出所有的 2 交换至数组的尾部
    # 当我们找到 2 时，我们需要不断地将其与 nums[p2] 进行交换，直到新的 nums[i] 不为 2
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        p0, p2 = 0, n - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/sort-colors/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。