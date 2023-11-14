class Solution:
    # low performance
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return '11'

        res = ["1", "1"]
        for i in range(3, n + 1):
            distinct_num = set(res)
            if len(distinct_num) == 1:
                res = [str(len(res)), res[0]]
            elif len(distinct_num) == len(res):
                for j in range(len(res)):
                    j *= 2
                    res[j:] = ["1"] + res[j:]
                    # print(res, j)
            else:
                # print(res)
                original_len = len(res)
                j = 0
                while j < original_len:
                    cur_num = res[j]
                    occurrence = 1
                    while j + 1 < original_len and res[j] == res[j + 1]:
                        occurrence += 1
                        j += 1
                        # print(j)
                    j += 1
                    res.append(str(occurrence))
                    res.append(cur_num)
                    # print(res)
                for k in range(original_len):
                    res.pop(0)

        return "".join(res)

    # 遍历
    def countAndSay(self, n: int) -> str:
        prev = "1"
        for i in range(n - 1):
            curr = ""
            pos = 0
            start = 0

            while pos < len(prev):
                while pos < len(prev) and prev[pos] == prev[start]:
                    pos += 1
                curr += str(pos - start) + prev[start]
                start = pos
            prev = curr

        return prev

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/count-and-say/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。