class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # res = [[1], [1, 1], [1, 2, 1]]

        # if numRows <= 2:
        #     return res[:numRows]

        # for i in range(3, numRows):
        #     newRow = [1, 1]
        #     for j in range(1, len(res[-1])):
        #         newRow.insert(j, res[-1][j] + res[-1][j-1])
        #     res.append(newRow)

        # return res

        # Create an array list to store the output result...
        output = []
        for i in range(numRows):
            if (i == 0):
                # Create a list to store the prev triangle value for further addition...
                # Inserting for the first row & store the prev array to the output array...
                prev = [1]
                output.append(prev)
            else:
                curr = [1]
                j = 1
                # Calculate for each of the next values...
                while (j < i):
                    # Inserting the addition of the prev arry two values...
                    curr.append(prev[j - 1] + prev[j])
                    j += 1
                # Store the number 1...
                curr.append(1)
                # Store the value in the Output array...
                output.append(curr)
                # Set prev is equal to curr...
                prev = curr
        return output  # Return the output list of pascal values...