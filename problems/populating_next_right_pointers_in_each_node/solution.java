/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    public Node connect(Node root) {
        LinkedList<Node> list = new LinkedList<>();
        list.add(root);
        list.add(null);
        while(!list.isEmpty()){
            Node current = list.getFirst();
            if(current ==null){
                return root;
            }
            list.add(current.left);
            list.add(current.right);
            if(list.get(1)==null){
                current.next = null;
                list.add(null);
                list.removeFirst();
                list.removeFirst();
            }
            else{
                current.next = list.get(1);
                list.removeFirst();
            }
        }
        return root;
    }
}