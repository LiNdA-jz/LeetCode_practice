class Solution:
    def romanToInt(self, s: str) -> int:
        # rToInt_dict = {
        #     "I": 1,
        #     "V": 5,
        #     "X": 10,
        #     "L": 50,
        #     "C": 100,
        #     "D": 500,
        #     "M": 1000
        # }

        # num = rToInt_dict[s[0]]
        # for i in range(1, len(s)):
        #     if (rToInt_dict[s[i]] <= rToInt_dict[s[i-1]]):
        #         num += rToInt_dict[s[i]]
        #     else:
        #         num -= rToInt_dict[s[i-1]]
        #         num += (rToInt_dict[s[i]] - rToInt_dict[s[i-1]])

        # return num

        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number