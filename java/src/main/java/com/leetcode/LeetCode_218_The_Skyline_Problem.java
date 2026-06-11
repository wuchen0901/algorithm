package com.leetcode;

import java.util.*;

public class LeetCode_218_The_Skyline_Problem {
    static class Event {

        int x;

        public static final int TYPE_START = 0;
        public static final int TYPE_END = 1;

        int type;

        int height;

        Event(int x, int type, int height) {
            this.x = x;
            this.type = type;
            this.height = height;
        }
    }

    public List<List<Integer>> getSkyline(int[][] buildings) {
        List<Event> events = new ArrayList<>(buildings.length * 2);

        for (int[] building : buildings) {
            events.add(new Event(building[0], Event.TYPE_START, building[2]));
            events.add(new Event(building[1], Event.TYPE_END, building[2]));
        }

        Collections.sort(events, (e1, e2) -> {
            if (e1.x != e2.x) {
                return Integer.compare(e1.x, e2.x);
            }

            if (e1.type != e2.type) {
                return e1.type - e2.type; // START before END, if START = 0, END = 1
            }

            if (e1.type == Event.TYPE_START) {
                return Integer.compare(e2.height, e1.height); // higher start first
            } else {
                return Integer.compare(e1.height, e2.height); // lower end first
            }
        });

        TreeMap<Integer, Integer> heights = new TreeMap<>();
        heights.put(0, 1); // ground height

        List<List<Integer>> result = new ArrayList<>();
        int prevMax = 0;

        for (Event event : events) {
            if (event.type == Event.TYPE_START) {
                heights.put(event.height, heights.getOrDefault(event.height, 0) + 1);
            } else {
                int count = heights.get(event.height);
                if (count == 1) {
                    heights.remove(event.height);
                } else {
                    heights.put(event.height, count - 1);
                }
            }

            int curMax = heights.lastKey();

            if (curMax != prevMax) {
                result.add(Arrays.asList(event.x, curMax));
                prevMax = curMax;
            }
        }

        return result;
    }
}
