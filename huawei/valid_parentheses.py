class Solution:
    def isValid(self, s: str) -> bool:
        # left_valid = ['(', '{', '[']
        # stack = []

        # for i in s:
        #     if i in left_valid:
        #         stack.append(i)
        #     elif i == ')':
        #         if len(stack) == 0:
        #             return False
        #         elif stack[-1] != '(':
        #             return False
        #         else:
        #             stack.pop(-1)
        #     elif i == '}':
        #         if len(stack) == 0:
        #             return False
        #         elif stack[-1] != '{':
        #             return False
        #         else:
        #             stack.pop(-1)
        #     elif i == ']':
        #         if len(stack) == 0:
        #             return False
        #         elif stack[-1] != '[':
        #             return False
        #         else:
        #             stack.pop(-1)

        # return True if len(stack) == 0 else False

        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/valid-parentheses/solution/you-xiao-de-gua-hao-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。