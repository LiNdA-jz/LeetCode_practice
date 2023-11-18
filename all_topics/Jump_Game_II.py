class Solution:
    # low performance
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        elif nums[0] >= len(nums) - 1:
            return 1

        res = [0] * (len(nums))
        for i in range(len(nums)):
            res[i] += i
        # print(res)

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            # print(prev)
            if prev >= len(nums) - i:
                return min(res[-1], res[i - 1] + 1)
            else:
                j = i
                while j < i + prev and j < len(nums):
                    res[j] = min(res[j], res[i - 1] + 1)
                    # print(res)
                    j += 1
        # print(res)

        return res[-1]

    # 如果某一个作为 起跳点 的格子可以跳跃的距离是 3，那么表示后面 3 个格子都可以作为 起跳点。 11. 可以对每一个能作为 起跳点 的格子都尝试跳一次，把 能跳到最远的距离 不断更新。

    # 如果从这个 起跳点 起跳叫做第 1 次 跳跃，那么从后面 3 个格子起跳 都 可以叫做第 2 次 跳跃。

    # 所以，当一次 跳跃 结束时，从下一个格子开始，到现在 能跳到最远的距离，都 是下一次 跳跃 的 起跳点。 31. 对每一次 跳跃 用 for 循环来模拟。

    # 跳完一次之后，更新下一次 起跳点 的范围。
    # 在新的范围内跳，更新 能跳到最远的距离。
    # 记录 跳跃 次数，如果跳到了终点，就得到了结果。

    # 作者：Ikaruga
    # 链接：https://leetcode.cn/problems/jump-game-ii/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    def jump(self, nums: List[int]) -> int:
        ans, start, end = 0, 0, 1

        while (end < len(nums)):
            maxPos = 0

            for i in range(start, end):
                maxPos = max(maxPos, i + nums[i])

            start = end
            end = maxPos + 1
            ans += 1

        # optimise
        ans, end, maxPos = 0, 0, 0

        for i in range(len(nums) - 1):
            maxPos = max(nums[i] + i, maxPos)

            if (i == end):
                end = maxPos
                ans += 1

        return ans