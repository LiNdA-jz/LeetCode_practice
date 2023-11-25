class Solution:
    # NOT WORK, 203/210
    # def maxSubArray(self, nums: List[int]) -> int:
    #     if len(nums) <= 2:
    #         return max(sum(nums), max(nums))

    #     largest_sum = nums[0]

    #     l, mid, r = 0, 1, len(nums) - 1
    #     while r > l and nums[r] < 0:
    #         if nums[r] < 0:
    #             r -= 1

    #     if r - l <= 1:
    #         return max(sum(nums[l:r + 1]), max(nums))

    #     # print(len(nums), l, " ", r)

    #     while mid <= r:
    #         largest_sum = max(largest_sum, sum(nums[l:mid + 1]))
    #         while nums[l] < 0 and l < r - 1:
    #             l += 1
    #             mid = l + 1

    #         largest_sum = max(largest_sum, nums[l])

    #         while mid <= r and nums[mid] >= 0:
    #             largest_sum = max(largest_sum, sum(nums[l:mid + 1]))
    #             mid += 1

    #         while mid <= r and nums[mid] < 0 and sum(nums[l:mid + 1]) < 0:
    #             l = mid + 1
    #             mid = l + 1
    #             largest_sum = max(largest_sum, sum(nums[l:mid + 1]))

    #         mid += 1

    #         print(l, " ", mid, " ", largest_sum)

    #     return max(largest_sum, nums[r])

    # 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        pre, maxAns = 0, nums[0]

        for i in nums:
            pre = max(pre + i, i)
            maxAns = max(maxAns, pre)

        return maxAns

    # 分治
    # 如果我们把 [0,n−1] 分治下去出现的所有子区间的信息都用堆式存储的方式记忆化下来，
    # 即建成一棵真正的树之后，我们就可以在 O(log⁡n) 的时间内求到任意区间内的答案，
    # 我们甚至可以修改序列中的值，做一些简单的维护，之后仍然可以在 O(log⁡n) 的时间内
    # 求到任意区间内的答案，对于大规模查询的情况下，这种方法的优势便体现了出来。
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        return self.__max_sub_array(nums, 0, size - 1)

    def __max_sub_array(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) >> 1
        return max(self.__max_sub_array(nums, left, mid),
                   self.__max_sub_array(nums, mid + 1, right),
                   self.__max_cross_array(nums, left, mid, right))

    def __max_cross_array(self, nums, left, mid, right):
        # 一定包含 nums[mid] 元素的最大连续子数组的和，
        # 思路是看看左边"扩散到底"，得到一个最大数，右边"扩散到底"得到一个最大数
        # 然后再加上中间数
        left_sum_max = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:
            s1 += nums[start_left]
            left_sum_max = max(left_sum_max, s1)
            start_left -= 1

        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1
        return left_sum_max + nums[mid] + right_sum_max

# 作者：liweiwei1419
# 链接：https://leetcode.cn/problems/maximum-subarray/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。