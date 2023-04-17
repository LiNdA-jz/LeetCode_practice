class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # not work
        # if columnNumber < 27:
        #     return chr(columnNumber + 64)
        # else:
        #     col = ""
        #     num = columnNumber
        #     if num > 26:
        #         col += chr(num // 26 + 64)
        #         col += self.convertToTitle(num - (num // 26) * 26)

        #     else:
        #         col += chr(columnNumber + 64)

        #     return col

        # The first idea that come to mind is that
        # it's just a base change instead of base of 10
        # we change the number to base of 26.

        # Create an empty string for storing the characters...
        output = ""
        # Run a while loop while columnNumber is positive...
        while columnNumber > 0:
            # Subtract 1 from columnNumber and get current character by doing modulo of columnNumber by 26...
            output = chr(ord('A') + (columnNumber - 1) % 26) + output
            # Divide columnNumber by 26...
            columnNumber = (columnNumber - 1) // 26
        # Return the output string.
        return output