class Solution:
    # low performance in time
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        res = []
        if "" in strs:
            res.append([""] * strs.count(""))

        ascii_ls = []
        for i in range(len(strs)):
            ascii_ls.append(sorted([ord(i) for i in strs[i]]))

        while len(strs) > 0:
            if strs[0] == "":
                strs.pop(0)
                ascii_ls.pop(0)
                continue
            cur_group = [strs[0]]
            cur_word = ascii_ls[0]
            # print(cur_word)
            strs.pop(0)
            ascii_ls.pop(0)

            for idx in range(len(strs)):
                if ascii_ls[idx] == cur_word:
                    cur_group.append(strs[idx])
                    strs[idx] = ""

            res.append(cur_group)

        return res

    # 排序
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/group-anagrams/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 计数
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

        return list(mp.values())

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/group-anagrams/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。