package com.leetcode;

public class LeetCode_733_Flood_Fill {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] != color) {
            dfs(image, sr, sc, image[sr][sc], color);
        }

        return image;
    }

    void dfs(int[][] image, int sr, int sc, int originalColor, int targetColor) {
        if (image[sr][sc] != originalColor) {
            return;
        }

        image[sr][sc] = targetColor;

        int[][] directions = new int[][]{
                {1, 0},
                {-1, 0},
                {0, 1},
                {0, -1},
        };

        for (int[] direction : directions) {
            int dr = direction[0];
            int dc = direction[1];

            if (0 <= sr + dr && sr + dr < image.length && 0 <= sc + dc && sc + dc < image[sr + dr].length) {
                dfs(image, sr + dr, sc + dc, originalColor, targetColor);
            }
        }
    }
}
