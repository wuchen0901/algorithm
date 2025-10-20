package com.leetcode;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;

public class LeetCode_1091_Shortest_Path_in_Binary_Matrix {
    public int shortestPathBinaryMatrix(int[][] grid) {
        int n = grid.length;
        if(n == 1){
            if(grid[0][0] == 0){
                return 1;
            }
            else {
                return -1;
            }
        }
        Deque<int[]> queue = new ArrayDeque<>();
        int VISITED = 2;
        int UNVISITED = 0;

        // corner case when only one element
        queue.offer(new int[]{0,0});
        int count = 1;

        int[] directions = {};
        while(!queue.isEmpty()) {
            int size = queue.size();
            count++;
            for(int i = 0; i < size; i++) {
                int[] position = queue.poll();
                int row = position[0];
                int column = position[1];

                if(Math.abs(n - row) <= 1 && Math.abs(n - column) <= 1) {
                    return count;
                }
                if (0 <= row - 1){
                    if(grid[row - 1][column] == UNVISITED){
                        grid[row - 1][column] = VISITED;
                        queue.offer(new int[]{row-1,column});
                    }
                }
                if(0<= row -1 && 0<= column - 1){
                    if(grid[row - 1][column - 1] == UNVISITED){
                        grid[row - 1][column - 1] = VISITED;
                        queue.offer(new int[]{row-1,column-1});
                    }
                }
                if(0<= row - 1 && column + 1 < n){
                    if(grid[row - 1][column + 1] ==UNVISITED){
                        grid[row - 1][column + 1] = VISITED;
                        queue.offer(new int[]{row-1,column});
                    }
                }
                if( 0<=column - 1){
                    if(grid[row][column - 1] == UNVISITED){
                        grid[row][column - 1] = VISITED;
                        queue.offer(new int[]{row,column - 1});
                    }

                }
                if( column + 1< n){
                    if(grid[row][column + 1] == UNVISITED){
                        grid[row][column + 1] = VISITED;
                        queue.offer(new int[]{row,column+1});
                    }
                }
                if(row + 1 < n && 0<=column -1 ){
                    if(grid[row + 1][column - 1] == UNVISITED) {
                        grid[row + 1][column - 1] = VISITED;
                        queue.offer(new int[]{row + 1, column-1});
                    }
                }
                if(row + 1 < n){
                    if(grid[row + 1][column]== UNVISITED){
                        grid[row + 1][column] = VISITED;
                        queue.offer(new int[]{row+1,column});
                    }
                }
                if( row + 1 < n && column + 1 < n){
                    if(grid[row + 1][column + 1] == UNVISITED){
                        grid[row + 1][column + 1] = VISITED;
                        queue.offer(new int[]{row+1, column + 1});
                    }
                }
            }
        }

        return -1;
    }
}
