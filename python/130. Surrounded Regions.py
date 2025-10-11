from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows, cols = len(board), len(board[0])

        # Return:
        # - True : Replace or haven't decided yet.
        # - False: Don't replace it.

        # Use a set to store all the positions traversed, when we get the result, replace them.
        # visited = set()
        # We need two sets, one for the current iteration.
        # The other is for all iterations.
        visiting = set()
        # The other is for the positions that don't have to replace.
        remaining = set()

        def dfs(i, j) -> bool:
            if not (0 <= i < rows and 0 <= j < cols):
                # We should do this outside this recursive function
                # remaining.update(visiting)
                return False  # No, for sure

            if board[i][j] == 'X':
                return True  # Not decided yet

            # We can't modify the grid map here because we haven't decided if we should replace it or not.
            # We'd better use a visited set instead.
            # if board[i][j] == 'O':
            #     board[i][j] = 'X'
            # if board[i][j] == 'O':  # Omit
            if (i, j) in visiting:
                return True  # Not decided yet
            visiting.add((i, j))

            # I found an error, these return values are ignored
            # dfs(i + 1, j)
            # dfs(i - 1, j)
            # dfs(i, j + 1)
            # dfs(i, j - 1)

            return dfs(i + 1, j) and dfs(i - 1, j) and dfs(i, j + 1) and dfs(i, j - 1)

            # Replace
            # for i, j in visiting:
            #     board[i][j] = 'X'
            #
            # return True  # Yes, for sure
            #
            # We should do that outside of this recursive function

        # There should be a collection, which stores the positions that should not be replaced.
        # remaining = set()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in remaining:
                    if dfs(r, c):
                        for (i, j) in visiting:
                            board[i][j] = 'X'
                    else:
                        remaining.update(visiting)
                    visiting.clear()
                    # Is it necessary to use two sets?
                    # Yes, if not, we have to replace too many positions into 'X' after each iteration.