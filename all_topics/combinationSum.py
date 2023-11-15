class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0,[],0)
        return res

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < min(candidates):
            return []

        res = []
        for i in range(len(candidates)):
            cur_sum = candidates[i]
            cur_num_count = 1

            while cur_sum <= target:
                if cur_sum == target:
                    res.append([candidates[i]] * cur_num_count)
                    # print(res)
                    break
                else:
                    diff = target - cur_sum
                    if i != len(candidates) - 1:
                        sub_comb = self.combinationSum(candidates[i + 1:], diff)
                        if len(sub_comb) != 0:
                            for next_comb in sub_comb:
                                res.append([candidates[i]] * cur_num_count + next_comb)
                                # print(res)
                    cur_sum += candidates[i]
                    cur_num_count += 1

        return res