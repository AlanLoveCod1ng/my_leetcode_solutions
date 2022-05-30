class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int min = Integer.MAX_VALUE;
        int minIndex = -1;
        int sum = 0;
        for(int i = 0; i< cost.length; i++){
            int current = gas[i] - cost[i];
            sum+=current;
            if(sum<min){
                min = sum;
                minIndex = i;
            }
        }
        return sum>=0?(minIndex+1)%gas.length:-1;
    }
}