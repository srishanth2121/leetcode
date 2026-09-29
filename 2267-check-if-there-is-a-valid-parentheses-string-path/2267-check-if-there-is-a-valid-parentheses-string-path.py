class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # Starting with ')' is immediately invalid
        if grid[0][0] == ')':
            return False

        # dp[c] contains all possible balances at the current row/cell
        dp = [[set() for _ in range(n)] for _ in range(m)]

        dp[0][0].add(1)

        for r in range(m):
            for c in range(n):

                if r == 0 and c == 0:
                    continue

                if grid[r][c] == '(':
                    change = 1
                else:
                    change = -1

                # From the cell above
                if r > 0:
                    for balance in dp[r - 1][c]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

                # From the cell on the left
                if c > 0:
                    for balance in dp[r][c - 1]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            dp[r][c].add(new_balance)

        return 0 in dp[m - 1][n - 1]