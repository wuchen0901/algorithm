package com.leetcode;

import java.util.*;

public class LeetCode_752_Open_the_Lock {
    public int openLock(String[] deadends, String target) {
        if (target.equals("0000"))
            return 0;


        Set<String> visited = new HashSet<>(Arrays.asList(deadends));

        if (visited.contains("0000"))
            return -1;

        Queue<String> queue = new ArrayDeque<>();


        queue.offer("0000");


        int steps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int s = 0; s < size; s++) {

                String code = queue.poll();

                for (int index = 0; index < 4; index++) {
                    char digit = code.charAt(index);
                    if (digit == '0') {
                        digit = '9';
                    } else {
                        digit--;
                    }

                    String prevCode = code.substring(0, index) + digit + code.substring(index + 1);

                    if (prevCode.equals(target)) {
                        return steps + 1;
                    }
                    if (!visited.contains(prevCode)) {
                        visited.add(prevCode);
                        queue.offer(prevCode);
                    }

                    digit = code.charAt(index);

                    if (digit == '9') {
                        digit = '0';
                    } else {
                        digit++;
                    }

                    String nextCode = code.substring(0, index) + digit + code.substring(index + 1);

                    if (nextCode.equals(target)) {
                        return steps + 1;
                    }

                    if (!visited.contains(nextCode)) {
                        visited.add(nextCode);
                        queue.offer(nextCode);
                    }
                }
            }
            steps++;
        }

        return -1;
    }
}
