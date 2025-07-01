from typing import List


# Classic fill algorithm (like Photoshop’s paint bucket).
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]

        # If the starting pixel already has the new color, no need to do anything
        if original_color == color:
            return image

        def dfs(r: int, c: int):
            # If out of bounds or not the original color, stop
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original_color:
                return

            # Fill the pixel with the new color
            image[r][c] = color

            # Recursively call dfs in 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
