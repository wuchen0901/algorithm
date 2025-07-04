from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Solve the N-Queens problem and return all distinct solutions.

        Each solution contains a distinct board configuration of the n-queens placement,
        where 'Q' and '.' both indicate a queen and an empty space respectively.

        Args:
            n (int): Size of the board (n x n)

        Returns:
            List[List[str]]: All valid queen placements
        """
        result = []
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col

        def backtrack(path: List[int]) -> None:
            row = len(path)
            if row == n:
                board = [''.join('Q' if c == col else '.' for c in range(n)) for col in path]
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                path.append(col)
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(path)

                path.pop()
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack([])

        return result


if __name__ == '__main__':
    print(Solution().solveNQueens(4))
