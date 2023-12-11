class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        print(path)

        res = ["/"]

        slash = True
        for i in path:
            if i != "." and i != ".." and i != "":
                res.append(i)
                res.append("/")
            if i == "..":
                if len(res) != 1:
                    res.pop()
                    res.pop()
        print(res)

        return "".join(res[:-1]) if res != ["/"] else res[0]

    # 栈
    def simplifyPath(self, path: str) -> str:
        names = path.split("/")
        stack = list()
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/simplify-path/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。