class Solution:
    # 超出时间限制 24/27
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     if k == n:
    #         return [[i for i in range(1, n + 1)]]

    #     if k == 1:
    #         return [[i] for i in range(1, n + 1)]

    #     res = []

    #     for i in range(1, n + 1):
    #         next_comb = self.combine(n - 1, k - 1)[i - 1:]

    #         for j in next_comb:
    #             j = [1 + k for k in j]

    #             if i < min(j):
    #                 res.append([i] + j)

    #     # print(res)
    #     return res

    # 根据搜索起点画出二叉树
    # 深度优先遍历
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, track = [], []
        self.backtrack(n, k, 1, track, result)

        return result

    def backtrack(self, n, k, start, track, result):
        if len(track) == k:
            result.append(track[:])

        for i in range(start, n + 1):
            track.append(i)
            self.backtrack(n, k, i + 1, track, result)
            track.pop()

    # 递归
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        ans = []

        def dfs(cur, n, k):
            if len(temp) + (n - cur + 1) < k:
                return

            if len(temp) == k:
                # cannot use ans.append(temp)
                ans.append(temp[:])
                return

            # 考虑选择当前位置
            temp.append(cur)
            dfs(cur + 1, n, k)
            temp.pop()

            # 考虑不选择当前位置
            dfs(cur + 1, n, k)

        dfs(1, n, k)

        return ans

    # 非递归， 字典序法
    # 「对应的二进制数」一列包含了由 k 个 1 和 n−k 个 0 组成的所有二进制数，并且按照字典序排列
    # 找到它的字典序中的下一个数字：
    # 规则一：x 的最低位为 1，这种情况下，如果末尾由 t 个连续的 1，我们直接将倒数第 t 位的 1 和倒数第 t+1 位的 0 替换
    # 0011→0101，0101→0110，1001→1010，1001111→1010111
    # 规则二：x 的最低位为 0，这种情况下，末尾有 t 个连续的 0，而这 t 个连续的 0 之前有 m 个连续的 1，我们可以将倒数第 t+m 位置的 1 和倒数第 t+m+1 位的 0 对换，然后把倒数第 t+1 位到倒数第 t+m−1 位的 1 移动到最低位
    # 0110→1001，1010→1100，1011100→1100011

    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        ans = []

        # 初始化 -> 将temp 中[0, k - 1]每个位置i设置为i + 1， 末尾加一位n + 1作为哨兵
        for i in range(1, k + 1):
            temp.append(i)

        temp.append(n + 1)

        j = 0
        while j < k:
            ans.append(temp[:k])
            j = 0

            # 寻找第一个temp[j] + 1 != temp[j + 1] 的t
            while (j < k and temp[j] + 1 == temp[j + 1]):
                temp[j] = j + 1
                j += 1

            temp[j] += 1

        return ans