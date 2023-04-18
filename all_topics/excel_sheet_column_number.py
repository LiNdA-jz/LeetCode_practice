class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # if len(columnTitle) == 1:
        #     return ord(columnTitle) - 64
        # else:
        #     num = 0
        #     col_len = len(columnTitle)
        #     while col_len >= 1:
        #         num += 26 ** (len(columnTitle) - col_len) * (ord(columnTitle[col_len - 1]) - 64)
        #         col_len -= 1
        #     return num

        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter) - 64
            ans += digit * 26 ** pos
            pos += 1

        return ans