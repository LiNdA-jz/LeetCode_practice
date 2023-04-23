class Solution:
    def intToRoman(self, num: int) -> str:
        # res = ""
        # while num >= 1:
        #     if num >= 1000:
        #         res += "M" * (num // 1000)
        #         num = num % 1000
        #     elif num >= 500:
        #         if num >= 900:
        #             res += "CM"
        #             num -= 900
        #         else:
        #             res += "D"
        #             num = num % 500
        #     elif num >= 100:
        #         if num >= 400:
        #             res += "CD"
        #             num -= 400
        #         else:
        #             res += "C" * (num // 100)
        #             num = num % 100
        #     elif num >= 50:
        #         if num >= 90:
        #             res += "XC"
        #             num -= 90
        #         else:
        #             res += "L"
        #             num -= 50
        #     elif num >= 10:
        #         if num >= 40:
        #             res += "XL"
        #             num -= 40
        #         else:
        #             res += "X" * (num // 10)
        #             num = num % 10
        #     elif num >= 5:
        #         if num >= 9:
        #             res += "IX"
        #             num -= 9
        #         else:
        #             res += "V"
        #             num -= 5
        #     else:
        #         if num >= 4:
        #             res += "IV"
        #             num -= 4
        #         else:
        #             res += "I" * num
        #             num -= num

        # return res

        # Creating Dictionary for Lookup
        num_map = {
            1: "I",
            5: "V", 4: "IV",
            10: "X", 9: "IX",
            50: "L", 40: "XL",
            100: "C", 90: "XC",
            500: "D", 400: "CD",
            1000: "M", 900: "CM",
        }

        # Result Variable
        r = ''

        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num -= n
        return r