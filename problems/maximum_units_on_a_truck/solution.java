class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        PriorityQueue<int[]> queue = new PriorityQueue<>(10, (a, b) -> b[1] - a[1]);
        for (int[] box : boxTypes) {
            queue.add(box);
        }
        int currentSize = 0;
        int currentUnit = 0;
        while (!queue.isEmpty()) {
            int[] box = queue.poll();
            if (box[0] <= truckSize - currentSize) {
                currentUnit += box[0] * box[1];
                currentSize += box[0];
            } else {
                currentUnit += (truckSize - currentSize) * box[1];
                break;
            }
        }
        return currentUnit;
    }
}
