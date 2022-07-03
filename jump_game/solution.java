class Solution {
    //dp
    // public boolean canJump(int[] nums) {
    //     int [] dp = new int[nums.length];
    //     dp[0] = 1;
    //     for(int i = 0; i<nums.length; i++){
    //         int length = nums[i];
    //         if(dp[i]==0){
    //             return false;
    //         }
    //         for(int j = i; j<=i+length&&j<nums.length; j++){
    //             dp[j] = 1;
    //         }
    //     }
    //     return true;
    // }
    //greedy
    public boolean canJump(int[] nums) {
        int lastIndex = nums.length-1;
        for(int i = nums.length-1; i>=0; i--){
            if(nums[i]+i>=lastIndex){
                lastIndex = i;
            }
        }
        return lastIndex==0;
    }
}