class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_prod = -inf

        for i in range(n):
            cur = nums[i]
            if cur == 0:
                continue
            elif cur == 1:
                max_prod = max(max_prod, 1)
                continue
            max_prod = max(max_prod, cur)
            for j in range(i + 1, n):
                if nums[j] == 0:
                    max_prod = max(max_prod, 0)
                    break
                elif nums[j] == 1:
                    continue
                cur *= nums[j]
                max_prod = max(max_prod, cur)

        return max_prod

    # 动态规划
    # f_max(i) = max_{i = 1}^n{f(i - 1) * a_i, a_i}
    # 错误的 -> 并不满足「最优子结构」 -> 当前位置的最优解未必是由前一个位置的最优解转移得到的
    # 根据正负性进行分类讨论
        # 当前位置如果是一个负数的话，那么我们希望以它前一个位置结尾的某个段的积也是个负数，这样就可以负负得正，并且我们希望这个积尽可能「负得更多」，即尽可能小
        # 当前位置是一个正数的话，我们更希望以它前一个位置结尾的某个段的积也是个正数，并且希望它尽可能地大
        # 再维护一个 f_min(i) -> 表示以第 i 个元素结尾的乘积最小子数组的乘积
            # f_max(i) = max_{i = 1}^n{f_max(i - 1) * a_i, f_min(i - 1) * a_i, a_i}
            # f_min(i) = min_{i = 1}^n{f_max(i - 1) * a_i, f_min(i - 1) * a_i, a_i}
            # 代表第 i 个元素结尾的乘积最大子数组的乘积 f_max(i)

    # 时间复杂度和渐进空间复杂度都是 O(n)
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_f, min_f = [nums[0]] * n, [nums[0]] * n
        print(max_f, min_f)

        for i in range(1, n):
            max_f[i] = max(max_f[i - 1] * nums[i], max(nums[i], min_f[i - 1] * nums[i]))
            min_f[i] = min(min_f[i - 1] * nums[i], min(nums[i], max_f[i - 1] * nums[i]))

        print(max_f, min_f)
        return max(max_f)


    # 第 i 个状态只和第 i−1 个状态相关, 可以只用两个变量来维护 i−1 时刻的状态，一个维护 f_max ，一个维护 f_min
    # 空间复杂度O(1)
    def maxProduct(self, nums: List[int]) -> int:
        max_f, min_f, ans = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            mx, mn = max_f, min_f

            max_f = max(mx * nums[i], max(nums[i], mn * nums[i]))
            min_f = min(mn * nums[i], min(nums[i], mx * nums[i]))

            ans = max(ans, max_f)

        return ans