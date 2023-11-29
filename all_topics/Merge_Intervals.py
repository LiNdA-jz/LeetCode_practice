class Solution:
    # low performance
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return [intervals[0]]

        # sort
        for i in range(1, len(intervals)):
            j = i
            while intervals[j][0] < intervals[j - 1][0] and j >= 1:
                intervals[j - 1], intervals[j] = intervals[j], intervals[j - 1]
                j -= 1
        # print(intervals)

        intervals_long = []
        res = []
        for i in intervals:
            intervals_long.append(i[0])
            intervals_long.append(i[1])

        start, end = intervals[0][0], intervals[0][1]
        idx = 2
        while idx < len(intervals_long):
            cur_start, cur_end = intervals_long[idx], intervals_long[idx + 1]
            # print(start, end)
            if cur_start >= start and cur_start <= end:
                end = max(end, cur_end)
                # print("cond 1", start, end)
                idx += 2
            if cur_start > end:
                # if start != end:
                res.append([start, end])
                start, end = cur_start, cur_end
                # print("cond 2", start, end)
                idx += 2
            if idx >= len(intervals_long):
                res.append([start, end])
                # print("cond 3", start, end)

        return res

    # 排序
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/merge-intervals/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。