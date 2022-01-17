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
    List<List<Integer>> superList = new ArrayList<>();
    public List<List<Integer>> findLeaves(TreeNode root) {
        postOrder(root);
        return superList;
    }
    public int postOrder(TreeNode current){
        int leftHeight = -1;
        int rightHeight = -1;
        if(current.left!=null){
            leftHeight = postOrder(current.left);
        }
        if(current.right!=null){
            rightHeight = postOrder(current.right);
        }
        int currentHeight = Math.max(leftHeight, rightHeight)+1;
        visitCurrent(currentHeight, current.val);
        return currentHeight;
    }
    public void visitCurrent(int currentHeight, int value){
        if(superList.size()-1<currentHeight){
            List<Integer> list = new LinkedList<>();
            superList.add(list);
        }
        superList.get(currentHeight).add(value);
    }
}