class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        res = []
        [start, end] = newInterval
        for i in range(len(intervals)):
            # print(start, end)

            if end < intervals[i][0]:
                res.append([start, end])
                return res + intervals[i:]
            if start > intervals[i][1]:
                if i == len(intervals) - 1:
                    return res + [intervals[i]] + [[start, end]]
                res = res + [intervals[i]]
                continue

            start = min(start, intervals[i][0])

            if end > intervals[i][1]:
                if i == len(intervals) - 1:
                    return res + [[start, end]]
                else:
                    continue
            else:
                end = max(end, intervals[i][1])
                res.append([start, end])
                return res + intervals[i + 1:]

        return res

    # 模拟
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)

        if not placed:
            ans.append([left, right])
        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/insert-interval/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。