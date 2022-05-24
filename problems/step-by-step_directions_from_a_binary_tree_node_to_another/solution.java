/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public String getDirections(TreeNode root, int startValue, int destValue) {
        ArrayList<String> results = DFS(root,destValue,startValue);
        String pathToDest = results.get(0);
        String pathToStart = results.get(1);
        while(pathToDest.length()!=0 && pathToStart.length()!=0&&pathToDest.charAt(0)==pathToStart.charAt(0)){
            pathToStart = pathToStart.substring(1);
            pathToDest = pathToDest.substring(1);
        }
        return pathToStart.replaceAll(".","U")+pathToDest;
    }
    public ArrayList<String> DFS(TreeNode current, int dest, int start){
//         if(current.val==goal){   
//             return path;
//         }
//         String leftPath = null;
//         String rightPath = null;
//         if(current.left!=null){
//             leftPath = DFS(current.left,goal,path+"L");
//         }
//         if(current.right!=null){
//             rightPath = DFS(current.right,goal,path+"R");
//         }
        
//         if(leftPath!=null)return leftPath;
//         else if(rightPath!=null)return rightPath;
//         return null;
        ArrayList<String> results = new ArrayList<>();
        String destPath = null;
        String startPath = null;
        Stack<State>stack = new Stack<>();
        stack.push(new State("",current));
        while(!stack.isEmpty()){
            State currentState = stack.pop();
            TreeNode node = currentState.node;
            String path = currentState.path;
            if(node.val == start){
                startPath = path;
            }
            if(node.val == dest){
                destPath = path;
            }
            if(startPath!=null&&destPath!=null){
                results.add(destPath);
                results.add(startPath);
                return results;
            }
            if(node.left!=null){
                stack.push(new State(path+"L",node.left));
            }
            if(node.right!=null){
                stack.push(new State(path+"R",node.right));
            }
        }
        return null;
    }
}
class State{
    String path;
    TreeNode node;
    State(String path, TreeNode node){
        this.path = path;
        this.node = node;
    }
}