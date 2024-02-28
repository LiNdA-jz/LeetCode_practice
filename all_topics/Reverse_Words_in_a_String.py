class Solution:
    def reverseWords(self, s: str) -> str:
        word_ls = s.strip().split(" ")[::-1]
        # print(word_ls)

        res = ""
        for i in word_ls:
            if i != "":
                res += i + " "

        return res.strip()

    # 使用语言特性
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    # 作者：力扣官方题解
    # 链接：https://leetcode.cn/problems/reverse-words-in-a-string/solutions/194450/fan-zhuan-zi-fu-chuan-li-de-dan-ci-by-leetcode-sol/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    # 自行编写对应的函数
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # 去掉字符串开头的空白字符
        while left <= right and s[left] == ' ':
            left += 1

        # 去掉字符串末尾的空白字符
        while left <= right and s[right] == ' ':
            right -= 1

        # 将字符串间多余的空白字符去除
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # 循环至单词的末尾
            while end < n and l[end] != ' ':
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # 更新start，去找下一个单词
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        l = self.trim_spaces(s)

        # 翻转字符串
        self.reverse(l, 0, len(l) - 1)

        # print(l)

        # 翻转每个单词
        self.reverse_each_word(l)

        print(l)
        return ''.join(l)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/reverse-words-in-a-string/solutions/194450/fan-zhuan-zi-fu-chuan-li-de-dan-ci-by-leetcode-sol/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。