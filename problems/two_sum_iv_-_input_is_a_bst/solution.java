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
    Set<Integer> set= new HashSet<>();
    boolean result = false;
    public boolean findTarget(TreeNode root, int k) {
        preTravesal(root, k);
        return result;
    }
    void preTravesal(TreeNode root, int k){
        if(set.contains(root.val)){
            result = true;
        }
        set.add(k-root.val);
        if(root.left!=null&&!result){
            preTravesal(root.left, k);
        }
        if(root.right!=null&&!result){
            preTravesal(root.right, k);
        }
    }
}