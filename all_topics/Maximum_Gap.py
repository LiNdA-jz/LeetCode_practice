class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        max_gap = 0
        nums.sort()

        # print(nums)
        for i in range(1, n):
            max_gap = max(max_gap, nums[i] - nums[i - 1])

        return max_gap

    # 基数排序
    # 将数组排序后再找出最大间距, （快速排序、归并排序等）均需要 O(Nlog⁡N) 的时间复杂度
    # 时间复杂度：O(N)
    # 空间复杂度：O(N)
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        exp = 1
        buf = [0] * n
        # print(buf)
        max_val = max(nums)

        while max_val >= exp:
            cnt = [0] * 10

            for i in range(n):
                digit = int((nums[i] / exp) % 10)
                cnt[digit] += 1

            for i in range(1, 10):
                cnt[i] += cnt[i - 1]

            for i in range(n - 1, -1, -1):
                digit = int((nums[i] / exp) % 10)
                buf[cnt[digit] - 1] = nums[i]
                cnt[digit] -= 1

            nums = buf.copy()
            exp *= 10

        ret = 0
        for i in range(1, n):
            ret = max(ret, nums[i] - nums[i - 1])

        return ret

    # 基于桶的算法
    # 相邻数字的最大间距不会小于 ⌈(max−min)/(N−1)⌉
    # 选取整数 d=⌊(max−min)/(N−1)⌋<⌈(max−min)/(N−1)⌉, 将整个区间划分为若干个大小为 d 的桶, 并找出每个整数所在的桶
    # 元素之间的最大间距一定不会出现在某个桶的内部，而一定会出现在不同桶当中
    # 维护每个桶内元素的最大值与最小值, 从前到后不断比较相邻的桶, 后一个桶的最小值与前一个桶的最大值
    # 时间复杂度：O(N)
    # 空间复杂度：O(N)
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        d = max(1, (max_val - min_val) // (n - 1))
        bucket_size = (max_val - min_val) // d + 1

        bucket = [[-1 for _ in range(2)] for _ in range(bucket_size)]
        # bucket = [[-1, -1]] * bucket_size
        # print(bucket)

        for i in range(n):
            idx = (nums[i] - min_val) // d

            if bucket[idx][0] == -1:
                bucket[idx][0] = bucket[idx][1] = nums[i]
            else:
                bucket[idx][0] = min(bucket[idx][0], nums[i])
                bucket[idx][1] = max(bucket[idx][1], nums[i])

        ret = 0
        prev = -1

        for i in range(bucket_size):
            if bucket[i][0] == -1:
                continue
            if prev != -1:
                ret = max(ret, bucket[i][0] - bucket[prev][1])
            prev = i

        return ret