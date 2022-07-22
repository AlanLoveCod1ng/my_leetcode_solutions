/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode head1 = null;
        ListNode tail1 = null;
        ListNode head2 = null;
        ListNode tail2 = null;
        ListNode current = head;
        while(current!=null){
            if(current.val<x){
                if(head1 == null){
                    head1 = current;
                }
                if(tail1 == null){
                    tail1 = current;
                }else{
                    tail1.next = current;
                    tail1 = current;
                }
            }
            else{
                if(head2 == null){
                    head2 = current;
                }
                if(tail2 == null){
                    tail2 = current;
                }else{
                    tail2.next = current;
                    tail2 = current;
                }
            }
            current = current.next;
        }
        if(tail1!=null)tail1.next = head2;
        else return head2;
        if(tail2!=null)tail2.next=null;
        if(head1==null)return null;
        return head1;
    }
}