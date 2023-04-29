class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # not work
        # if len(intervals) == 1:
        #     return intervals
        # cur_left, cur_right = intervals[0]
        # res = []

        # for i in range(1 ,len(intervals)):
        #     if (intervals[i][0] >= cur_left) and (intervals[i][0] <= cur_right) and (intervals[i][1] >= cur_right):
        #         cur_right = intervals[i][1]
        #         res.append([cur_left, cur_right])
        #     elif intervals[i][0] > cur_right:
        #         if [cur_left, cur_right] not in res:
        #             res.append([cur_left, cur_right])
        #         cur_left, cur_right = intervals[i]
        #         res.append([cur_left, cur_right])
        #     elif intervals[i][0] < cur_left:
        #         if intervals[i][1] >= cur_right:
        #             cur_left, cur_right = intervals[i]
        #             res.append([cur_left, cur_right])
        #         elif intervals[i][1] < cur_left:
        #             res.append(intervals[i])
        #             if [cur_left, cur_right] not in res:
        #                 res.append([cur_left, cur_right])
        #         else:
        #             cur_left = intervals[i][0]
        #             res.append([cur_left, cur_right])
        #     else:
        #         # cur_left, cur_right = intervals[i]
        #         res.append([cur_left, cur_right])
        #     # res.append([cur_left, cur_right])

        # return res

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

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/SsGoHC/solution/he-bing-qu-jian-by-leetcode-solution-ghjl/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。