class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        op = ["+", "-", "*", "/"]
        num_stack = []

        for i in tokens:
            if i not in op:
                num_stack.append(int(i))
            else:
                num2 = num_stack.pop()
                num1 = num_stack.pop()

                if i == "+":
                    num_stack.append(num1 + num2)
                elif i == "-":
                    num_stack.append(num1 - num2)
                elif i == "*":
                    num_stack.append(num1 * num2)
                else:
                    temp = num1 / num2
                    if abs(temp) < 0:
                        num_stack.append(0)
                    else:
                        num_stack.append(int(temp))

        return num_stack[-1]

    # 栈
    # 如果遇到操作数，则将操作数入栈
    # 如果遇到运算符，则将两个操作数出栈，其中先出栈的是右操作数，后出栈的是左操作数，使用运算符对两个操作数进行运算，将运算得到的新操作数入栈。
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y),   # 需要注意 python 中负数除法的表现与题目不一致
        }

        stack = list()
        for token in tokens:
            try:
                num = int(token)
            except ValueError:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            finally:
                stack.append(num)

        return stack[0]

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/evaluate-reverse-polish-notation/solutions/667892/ni-bo-lan-biao-da-shi-qiu-zhi-by-leetcod-wue9/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 数组模拟栈
    # 预先定义数组的长度, 对于一个有效的逆波兰表达式，其长度 n 一定是奇数，且操作数的个数一定比运算符的个数多 1 个, 即包含 (n + 1) / 2 个操作数和 (n - 1) / 2 个运算符
    # 如果遇到操作数，则将操作数入栈，因此栈内元素增加 1 个
    # 如果遇到运算符，则将两个操作数出栈，然后将一个新操作数入栈，因此栈内元素先减少 2 个再增加 1 个，结果是栈内元素减少 1 个
    # 最坏情况下，(n + 1) / 2 个操作数都在表达式的前面，(n - 1) / 2 个运算符都在表达式的后面，此时栈内元素最多为 (n + 1) / 2 个。在其余情况下，栈内元素总是少于 (n + 1) / 2 个。
    # 数组下标 0 的位置对应栈底，定义 index 表示栈顶元素的下标位置，初始时栈为空，index=−1
    # 如果遇到操作数，则将 index\textit{index}index 的值加 111，然后将操作数赋给 stack[index]
    # 如果遇到运算符，则将 index 的值减 1，此时 stack[index] 和 stack[index+1] 的元素分别是左操作数和右操作数，使用运算符对两个操作数进行运算，将运算得到的新操作数赋给 stack[index]
    def evalRPN(self, tokens: List[str]) -> int:
        op_to_binary_fn = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": lambda x, y: int(x / y),  # 需要注意 python 中负数除法的表现与题目不一致
        }

        n = len(tokens)
        stack = [0] * ((n + 1) // 2)
        index = -1
        for token in tokens:
            try:
                num = int(token)
                index += 1
                stack[index] = num
            except ValueError:
                index -= 1
                stack[index] = op_to_binary_fn[token](stack[index], stack[index + 1])

        return stack[0]

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/evaluate-reverse-polish-notation/solutions/667892/ni-bo-lan-biao-da-shi-qiu-zhi-by-leetcod-wue9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。