class Solution:
    # 4/8
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        else:
            res = []
            cur_n = n
            for i in range(1, n+1):
                for j in range(2, n+1):
                    if i % j == 0 and i != j:
                        repeat_n = i // j
                        if ("(" * repeat_n + ")" * repeat_n) * j not in res:
                            res.append(("(" * repeat_n + ")" * repeat_n) * j)
            remain = self.generateParenthesis(cur_n-1)
            for i in remain:
                if "(" + i + ")" not in res:
                    res.append("(" + i + ")")
                remain_n = n - cur_n
                if "(" * (remain_n + 1) + ")" * (remain_n + 1) + i not in res:
                    res.append("(" * (remain_n + 1) + ")" * (remain_n + 1) + i)
                if i + "(" * (remain_n + 1) + ")" * (remain_n + 1) not in res:
                    res.append(i + "(" * (remain_n + 1) + ")" * (remain_n + 1))

            return res

    # generate all combinations then check
    """
    ['(']
    ['(', '(']
    ['(', '(', '(']
    ['(', '(', '(', ')']
    ['(', '(', '(', ')', ')']
    ['(', '(', '(', ')', ')', ')']
    ['(', '(', '(', ')', ')']
    ['(', '(', '(', ')']
    """
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                print(A)
                A.pop()
                A.append(')')
                generate(A)
                print(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate([])
        return ans

# # 作者：力扣官方题解
# # 链接：https://leetcode.cn/problems/generate-parentheses/
# # 来源：力扣（LeetCode）
# # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    """
    ['(']
    ['(', '(']
    ['(', '(', '(']
    ['(', '(', '(', ')']
    ['(', '(', '(', ')', ')']
    ['(', '(', '(', ')', ')', ')']
    ['(', '(', '(', ')', ')']
    ['(', '(', '(', ')']
    """
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                # print(S)
                backtrack(S, left+1, right)
                S.pop()
                # print(S)
            if right < left:
                S.append(')')
                # print(S)
                backtrack(S, left, right+1)
                S.pop()
                # print(S)

        backtrack([], 0, 0)
        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/generate-parentheses/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。