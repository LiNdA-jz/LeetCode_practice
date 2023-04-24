# 二分查找+贪心
from sortedcontainers import SortedList


class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()

        def check(mid: int) -> bool:
            p = pills
            #  工人的有序集合
            ws = SortedList(workers[m - mid:])
            # 从大到小枚举每一个任务!!!!!!!!!!!
            for i in range(mid - 1, -1, -1):
                # 如果有序集合中最大的元素大于等于 tasks[i]
                if ws[-1] >= tasks[i]:
                    ws.pop()
                else:
                    if p == 0:
                        return False
                    rep = ws.bisect_left(tasks[i] - strength)
                    if rep == len(ws):
                        return False
                    p -= 1
                    ws.pop(rep)
            return True

        left, right, ans = 1, min(m, n), 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / maximum - number - of - tasks - you - can - assign / solution / ni - ke - yi - an - pai - de - zui - duo - ren - wu - shu - mu - p7dm /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。