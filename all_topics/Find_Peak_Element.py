class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        if right - left <= 1:
            return right if nums[right] > nums[left] else left

        while left < right:
            mid = left + (right - left) // 2
            # print(mid)

            cur_left, cur_right = mid - 1, mid + 1

            if nums[mid] > nums[cur_left] and nums[mid] > nums[cur_right]:
                return mid
            elif nums[mid] > nums[cur_left]:
                left = mid + 1
            else:
                right = mid

        return left

    # 寻找最大值
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[idx]:
                idx = i
        return idx

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/find-peak-element/solutions/998152/xun-zhao-feng-zhi-by-leetcode-solution-96sj/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 迭代爬坡
    # 如果我们从一个位置开始，不断地向高处走，那么最终一定可以到达一个峰值位置
    # 首先在 [0,n) 的范围内随机一个初始位置 i, 随后根据 nums[i−1], nums[i], nums[i+1] 三者的关系决定向哪个方向走
    # nums[i−1]<nums[i]>nums[i+1]: 直接返回
    # nums[i−1]<nums[i]<nums[i+1]: 往右走，即 i←i+1
    # nums[i−1]>nums[i]>nums[i+1]: 往左走，即 i←i−1
    # nums[i−1]>nums[i]<nums[i+1]: 两侧都是上坡，我们可以朝任意方向走
    # nums[i]<nums[i+1]: 往右走
    # nums[i]>nums[i+1]: 往左走

    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        idx = random.randint(0, n - 1)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        while not (get(idx - 1) < get(idx) > get(idx + 1)):
            if get(idx) < get(idx + 1):
                idx += 1
            else:
                idx -= 1

        return idx

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/find-peak-element/solutions/998152/xun-zhao-feng-zhi-by-leetcode-solution-96sj/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 方法二的二分查找优化
    # nums[i]<nums[i+1], 并且我们从位置 i 向右走到了位置 i+1, i 左侧的所有位置是不可能在后续的迭代中走到的
    # 对于当前可行的下标范围 [l,r]，我们随机一个下标 i
    # 如果下标 i 是峰值，我们返回 i
    # nums[i]<nums[i+1]: 在剩余 [i+1,r] 的范围内继续随机选取下标
    # nums[i]>nums[i+1]: 在剩余 [l,i−1] 的范围内继续随机选取下标

    # 时间复杂度：O(log⁡n)
    # 空间复杂度：O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # 辅助函数，输入下标 i，返回 nums[i] 的值
        # 方便处理 nums[-1] 以及 nums[n] 的边界情况
        def get(i: int) -> int:
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]

        left, right, ans = 0, n - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if get(mid - 1) < get(mid) > get(mid + 1):
                ans = mid
                break
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1

        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/find-peak-element/solutions/998152/xun-zhao-feng-zhi-by-leetcode-solution-96sj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。