class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            current_row = [1]

            if row >=2:
                previous_row = triangle[row - 1]

                for i in range(len(previous_row) - 1):
                    current_row.append(previous_row[i]  + previous_row[i+1])

            if row >0:
                current_row.append(1)

            triangle.append(current_row)

        return triangle


        