class MinStack:

    def __init__(self):
        self.stack = []
        self.cur_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.stack) == 1:
            self.cur_min.append(val)

        else:
            if val < self.cur_min[-1]:
                self.cur_min.append(val)
            else:
                self.cur_min.append(self.cur_min[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.cur_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.cur_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

    # 辅助栈
    # 在每个元素 a 入栈时把当前栈的最小值 m 存储起来
    # 设计一个数据结构，使得每个元素 a 与其相应的最小值 m 时刻保持一一对应
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/min-stack/solutions/242190/zui-xiao-zhan-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。