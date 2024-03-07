class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n <= 2:
            return n

        max_len = 1
        for i in range(n):
            cur_char = [s[i]]
            cur_len = 1

            for j in range(i + 1, n):
                if s[j] in cur_char:
                    cur_len += 1
                elif len(cur_char) == 2:
                    k = j
                    while k < n:
                        if s[k] in cur_char:
                            cur_len += 1
                            k += 1
                        else:
                            break
                    max_len = max(max_len, cur_len)
                    break
                else:
                    cur_char.append(s[j])
                    cur_len += 1

                max_len = max(max_len, cur_len)

                # print(max_len)

        return max_len

    # 滑动窗口
    # 设定两个指针 left 和 right 作为窗口的边界
    # 将两个指针都设定在位置 0， 然后向右移动 right 指针，直到 窗口内不超过两个不同的字符
    # 如果某一点我们得到了 3 个不同的字符， 那么需要移动 left 指针
    # 可以建立一个哈希表，键是滑动窗口中的所有字符，值是它们最右端的位置。在每一刻，这个哈希表最多只能包含 3 个元素
    # 如果字符串长度 N 小于 3，则返回 N
    # left = 0 和 right = 0 的位置，初始化最大子字符串长度 maxlen = 2
    # 当 right 指针小于 N 时
        # 如果哈希表包含少于 3 个不同的字符， 将当前字符 s[right] 添加到哈希表中， 并将 right 指针向右移动
        # 如果哈希表包含 3 个不同的字符， 从哈希表中删除最左侧的字符 并移动 left 指针，使得滑动窗口再次仅包含 2 个不同的字符
        # 更新 maxlen
    def lengthOfLongestSubstringTwoDistinct(self, s: 'str') -> 'int':
        n = len(s)
        if n < 3:
            return n

        # 滑动窗口的左右指针
        left, right = 0, 0
        # hashmap 中的字符 -> 它在滑动窗口中最靠右的位置
        hashmap = defaultdict()

        max_len = 2

        while right < n:
            # 当滑动窗口包含小于 3 个字符
            hashmap[s[right]] = right
            right += 1

            # 滑动窗口包含 3 个字符
            if len(hashmap) == 3:
                # 删除最左边的字符
                del_idx = min(hashmap.values())
                # print(hashmap.values(), del_idx)
                del hashmap[s[del_idx]]
                # 删除滑动窗口的左指针
                left = del_idx + 1

            max_len = max(max_len, right - left)

        return max_len

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/solutions/2388233/zhi-duo-bao-han-liang-ge-bu-tong-zi-fu-d-dqii/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。