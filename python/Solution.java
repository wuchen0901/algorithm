
class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        for (int i = 0; i < k; i++) {
            treeMap.put(nums[i], i);
        }

        double[] result = new double[nums.length - k + 1];
        for (int i = 0; i < nums.length - k + 1; i++) {
            Integer[] array = treeMap.keySet().toArray(new Integer[0]);
            result[i] = array[2];
        }
        return result;
    }
}