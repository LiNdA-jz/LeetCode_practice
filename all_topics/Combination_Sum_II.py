class Solution:
    # low performance
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # special cases
        if target < candidates[0] or target > sum(candidates):
            return []

        if target == sum(candidates):
            return [candidates]

        if len(set(candidates)) == 1:
            if target % candidates[0] == 0:
                return [[candidates[0]] * (target // candidates[0])]

        res = []
        i = 0
        while i < len(candidates):
            cur_sum = candidates[i]
            diff = target - cur_sum
            if diff == 0 and [candidates[i]] not in res:
                res.append([candidates[i]])

            if i < len(candidates) - 1:
                sub_comb = self.combinationSum2(candidates[i+1:], diff)
                # print(sub_comb)
                if len(sub_comb) != 0:
                    for comb in sub_comb:
                        cur_comb = [candidates[i]] + comb
                        if cur_comb not in res:
                            res.append(cur_comb)
                            if len(set(cur_comb)) == 1:
                                i += 1
                                while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                                    i += 1
                        # print(res)
            i += 1
        # print(res)
        return res

    # 递归 + 回溯
    # 哈希映射（HashMap）统计数组 candidates 中每个数出现的次数
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(pos: int, rest: int):
            nonlocal sequence
            if rest == 0:
                ans.append(sequence[:])
                return
            if pos == len(freq) or rest < freq[pos][0]:
                return

            dfs(pos + 1, rest)

            most = min(rest // freq[pos][0], freq[pos][1])
            for i in range(1, most + 1):
                sequence.append(freq[pos][0])
                dfs(pos + 1, rest - i * freq[pos][0])
            sequence = sequence[:-most]

        freq = sorted(collections.Counter(candidates).items())
        ans = list()
        sequence = list()
        dfs(0, target)
        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/combination-sum-ii/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。