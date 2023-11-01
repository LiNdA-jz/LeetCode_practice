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

    # practice on 01/11/2023
    # low performance
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        digit_list = []

        while num >= 1:
            digit_list.append((num % 10))
            num //= 10

        # print(digit_list)

        roman_list = []

        exp = 0
        for i in digit_list:
            cur_val = i * 10 ** exp
            if cur_val in roman_dict:
                roman_list.append(roman_dict[cur_val])
            elif i == 4:
                roman_list.append(roman_dict[5 * 10 ** exp])
                roman_list.append(roman_dict[10 ** exp])
            elif i == 9:
                roman_list.append(roman_dict[10 ** (exp + 1)])
                roman_list.append(roman_dict[10 ** exp])
            elif i < 5:
                for n in range(i):
                    roman_list.append(roman_dict[10 ** exp])
            else:
                j = i - 5
                for n in range(j):
                    roman_list.append(roman_dict[10 ** exp])
                roman_list.append(roman_dict[5 * 10 ** exp])

            exp += 1

        print(digit_list)

        return ''.join(roman_list[::-1])