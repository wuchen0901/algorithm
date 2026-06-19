package com.leetcode;

public class LeetCode_1109_Corporate_Flight_Bookings {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] diff = new int[n + 2];
        for (int[] booking : bookings) {
            int first = booking[0];
            int last = booking[1];
            int seats = booking[2];

            diff[first] += seats;
            diff[last + 1] -= seats;
        }

        int[] result = new int[n];
        result[0] = diff[1];
        for (int i = 1; i < result.length; i++) {
            result[i] = result[i - 1] + diff[i + 1];
        }
        return result;
    }
}
