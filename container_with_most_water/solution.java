class Solution {
    public int maxArea(int[] height) {
        int head = 0;
        int tail = height.length-1;
        int maxArea = 0;
        while(head<tail){
            maxArea = Math.max(maxArea, (tail-head)*Math.min(height[head],height[tail]));
            if(height[head]>height[tail]){
                tail--;
            }
            else if(height[head]<height[tail]){
                head++;
            }
            else{
                if(height[head+1]>height[tail-1]){
                    head++;
                }
                else{
                    tail--;
                }
            }
        }
        return maxArea;
    }
}