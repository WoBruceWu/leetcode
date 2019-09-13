class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.helper(grid, i, j)

        return res

    def helper(self, grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        if grid[row][col] == '0':
            return
        grid[row][col] = '0'
        self.helper(grid, row-1, col)
        self.helper(grid, row+1, col)
        self.helper(grid, row, col-1)
        self.helper(grid, row, col+1)