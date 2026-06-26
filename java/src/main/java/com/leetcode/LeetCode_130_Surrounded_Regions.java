package com.leetcode;

public class LeetCode_130_Surrounded_Regions {
    public void solve(char[][] board) {
        for (int r = 0; r < board.length; r++) {
            floodFill(board, r, 0, 'O', 'V');
            floodFill(board, r, board[r].length - 1, 'O', 'V');
        }

        for (int c = 0; c < board[0].length; c++) {
            floodFill(board, 0, c, 'O', 'V');
            floodFill(board, board.length - 1, c, 'O', 'V');
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                }
            }
        }

        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == 'V') {
                    floodFill(board, i, j, 'V', 'O');
                }
            }
        }
    }

    void floodFill(char[][] board, int r, int c, char original, char target) {
        if (board[r][c] != original) {
            return;
        }

        board[r][c] = target;

        int[][] directions = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int[] direction : directions) {
            int nr = r + direction[0];
            int nc = c + direction[1];

            if (0 <= nr && nr < board.length && 0 <= nc && nc < board[nr].length) {
                floodFill(board, nr, nc, original, target);
            }
        }
    }
}
