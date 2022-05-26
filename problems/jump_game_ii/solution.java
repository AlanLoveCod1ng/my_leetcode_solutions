class Solution {
    public int jump(int[] nums) {
        int [] record = new int[nums.length];
        for(int i = 0; i<nums.length; i++){
            for(int j = i+1; j-i <= nums[i]&&j<nums.length; j++){
                if(record[j]==0){
                    record[j]=record[i]+1;
                }
                record[j] = Math.min(record[i]+1,record[j]);
            }
        }
        return record[record.length-1];
    }
}