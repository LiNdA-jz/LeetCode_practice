class Solution:
    def isValid(self, s: str) -> bool:
        # if (len(s) % 2 == 1):
        #     return False

        # stack = []

        # for i in s:
        #     if (i == "("):
        #         stack.append(")")
        #     elif (i == "{"):
        #         stack.append("}")
        #     elif (i == "["):
        #         stack.append("]")
        #     elif (i == ")") or (i == "}") or (i == "]"):
        #         if (len(stack) == 0) or (stack.pop() != i):
        #             return False

        # return True if len(stack) == 0 else False

        # Create a pair of opening and closing parrenthesis...
        opcl = dict(('()', '[]', '{}'))
        # Create stack data structure...
        stack = []
        # Traverse each charater in input string...
        for idx in s:
            # If open parentheses are present, append it to stack...
            if idx in '([{':
                stack.append(idx)
            # If the character is closing parentheses, check that the same type opening parentheses is being pushed to the stack or not...
            # If not, we need to return false...
            elif len(stack) == 0 or idx != opcl[stack.pop()]:
                return False
        # At last, we check if the stack is empty or not...
        # If the stack is empty it means every opened parenthesis is being closed and we can return true, otherwise we return false...
        return len(stack) == 0