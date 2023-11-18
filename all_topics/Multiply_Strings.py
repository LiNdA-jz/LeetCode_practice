class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        num1_int, num2_int = 0, 0

        for i in range(len(num1) - 1, -1, -1):
            cur_pos = len(num1) - i - 1

            num1_int += (ord(num1[i]) - ord("0")) * (10 ** cur_pos)

        for i in range(len(num2) - 1, -1, -1):
            cur_pos = len(num2) - i - 1

            num2_int += (ord(num2[i]) - ord("0")) * (10 ** cur_pos)

        # print(num1_int, num2_int)

        # BigInteger!!!
        return str(num1_int * num2_int)

    # add
    # 1234 * 567 = 1234 * 7 + 1234 * 60 + 1234 * 500
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        ans = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            curr = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            ans = self.addStrings(ans, curr)

        return ans

    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            ans.append(str(result % 10))
            add = result // 10
            i -= 1
            j -= 1
        return "".join(ans[::-1])

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/multiply-strings/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # multifly
    # 令 m 和 n 分别表示 num1和 num2的长度，并且它们均不为 0，则 num1和 num2的乘积的长度为 m+n−1 或 m+n。简单证明如下：
    #
    # 如果 num1和 num2都取最小值，则 num1=10^(m−1)，num2=10^(n−1)，num1×num2=10^(m+n−2)，
    # 乘积的长度为 m+n−1；
    #
    # 如果 num1和 num2都取最大值，则 num1=10^m−1，num2=10^n−1，num1×num2=10^(m+n)−10m−10n+1，
    # 乘积显然小于 10^(m+n)且大于 10^(m+n−1)，
    # 因此乘积的长度为 m+n。
    #
    #
    #
    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/multiply-strings/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 1234 * 567 = 4 * 7 + 4 * 60 + 4 * 500 +
    # 30 * 7 + 30 * 60 + 30 * 500 +
    # 200 * 7 + 200 * 60 + 200 * 500 +
    # 1000 * 7 + 1000 * 60 + 1000 * 500
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        ansArr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ansArr[i + j + 1] += x * int(num2[j])

        for i in range(m + n - 1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10

        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/multiply-strings/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。