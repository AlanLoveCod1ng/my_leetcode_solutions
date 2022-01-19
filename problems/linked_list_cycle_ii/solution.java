/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
import java.util.*;
public class Solution {
    public ListNode detectCycle(ListNode head) {
        HashSet<ListNode> set = new HashSet<>();
        ListNode current = head;
        int size = set.size();
        while(current!=null){
            set.add(current);
            if(set.size()==size){
                return current;
            }
            size = set.size();
            current = current.next;
        }
        return null;
    }
}