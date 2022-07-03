class Solution {
    public boolean removeOnes(int[][] grid) {
        int [] flip = new int[grid[0].length];
        for(int i = 0; i<flip.length;i++){
            flip[i] = 1-grid[0][i];
        }
        for(int i = 0; i < grid.length; i++){
            if(!arrayEqual(grid[i],flip)&&!arrayEqual(grid[0],grid[i])){
                return false;
            }
        }
        return true;
    }
    public boolean arrayEqual(int [] a1, int [] a2){
        if(a1.length!=a2.length){
            return false;
        }
        for(int i = 0; i < a1.length; i++){
            if(a1[i]!=a2[i])
                return false;
        }
        return true;
    }
}