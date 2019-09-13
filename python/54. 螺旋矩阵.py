class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix) == 0: return []
        rowStart, rowEnd = 0, len(matrix)-1
        colStart, colEnd = 0, len(matrix[0])-1
        while rowStart <= rowEnd and colStart <= colEnd:
            for i in range(colStart, colEnd+1):
                res.append(matrix[rowStart][i])
            rowStart += 1

            for i in range(rowStart, rowEnd+1):
                res.append(matrix[i][colEnd])
            colEnd -= 1

            if rowStart <= rowEnd:
                # 假设输入只有一行，该操作保证不会从左走到右后再倒回来从右走到左
                for i in range(colStart, colEnd+1)[::-1]:
                    res.append(matrix[rowEnd][i])
                rowEnd -= 1

            if colStart <= colEnd:
                # 假设输入只有一列，该操作保证不会从上走到下后再倒回来从下走到上
                for i in range(rowStart, rowEnd+1)[::-1]:
                    res.append(matrix[i][colStart])
                colStart += 1

        return res