class Solution {
    
   public static int shortestPath(int[][] grid, int k) {
        LinkedList<State> queue= new LinkedList<>();
        Set<State> set = new HashSet<>();
        queue.add(new State(0,0,0,k));
       if (k >= grid.length + grid[0].length - 2) {
            return grid.length + grid[0].length - 2;
        }
        while(!queue.isEmpty()){
            State state = queue.poll();
            if(state.checkBoundary(grid.length,grid[0].length))
                continue;
            int x = state.x;
            int y = state.y;
            int moves = state.moves;
            int el = state.eliminateLeft;
            
            if(x==grid.length-1&&y==grid[0].length-1){
                return moves;
            }
            if(set.contains(state)){
                continue;
            }else{
                set.add(state);
            }
            //move right
            if(y<grid[0].length-1){
                if(grid[x][y+1]==1){
                    queue.add(new State(x,y+1,moves+1,el-1));
                }else{
                    queue.add(new State(x,y+1,moves+1,el));
                }
            }
            //move left
            if(y>0){
                if(grid[x][y-1]==1){
                    queue.add(new State(x,y-1,moves+1,el-1));
                }else{
                    queue.add(new State(x,y-1,moves+1,el));
                }
            }
            //move down
            if(x<grid.length-1){
                if(grid[x+1][y]==1){
                    queue.add(new State(x+1,y,moves+1,el-1));
                }else{
                    queue.add(new State(x+1,y,moves+1,el));
                }
            }
            
            //move up
            if(x>0){
                if(grid[x-1][y]==1){
                    queue.add(new State(x-1,y,moves+1,el-1));
                }else{
                    queue.add(new State(x-1,y,moves+1,el));
                }
            }
        }
        return -1;
    }
}
class State{
    int x;
    int y;
    int moves;
    int eliminateLeft;
    State(int x, int y, int moves, int eliminateLeft){
        this.x = x;
        this.y = y;
        this.moves = moves;
        this.eliminateLeft = eliminateLeft;
    }
    public boolean checkBoundary(int m, int n){
        if(this.x>=m||this.y>=n||this.eliminateLeft<0){
            return true;
        }
        return false;
    }
    @Override
    public boolean equals(Object obj) {
        State temp = (State)obj;
        if(this.x == temp.x && this.y == temp.y && this.eliminateLeft==temp.eliminateLeft){
            return true;
        }
        return false;
    }
    @Override
    public int hashCode() {
        int Y = this.y<<1;
        return this.x+ Y;
    }
}