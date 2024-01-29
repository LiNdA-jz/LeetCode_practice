class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0

        nums = sorted(set(nums))
        if len(nums) == 1:
            return 1

        ans = []
        cur_len = 1
        # print(nums)

        for i in range(1, len(nums)):
            if nums[i] != 1 + nums[i - 1]:
                # print(nums[i], nums[i - 1])
                ans.append(cur_len)
                cur_len = 1
            else:
                cur_len += 1
                if i == len(nums) - 1:
                    ans.append(cur_len)

        # print(ans)
        return max(ans)

    # 哈希表
    # 暴力的方法是 O(n) 遍历数组去看是否存在这个数，但其实更高效的方法是用一个哈希表存储数组中的数，这样查看一个数是否存在即能优化至 O(1) 的时间复杂度
    # 算法时间复杂度最坏情况下还是会达到 O(n^2)
    # 由于我们要枚举的数 x 一定是在数组中不存在前驱数 x−1 的，不然按照上面的分析我们会从 x−1 开始尝试匹配，因此我们每次在哈希表中检查是否存在 x−1 即能判断是否需要跳过了。
    # 外层循环需要 O(n) 的时间复杂度，只有当一个数是连续序列的第一个数的情况下才会进入内层循环, 然后在内层循环中匹配连续序列中的数, 数组中的每个数只会进入内层循环一次
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/longest-consecutive-sequence/solutions/276931/zui-chang-lian-xu-xu-lie-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。