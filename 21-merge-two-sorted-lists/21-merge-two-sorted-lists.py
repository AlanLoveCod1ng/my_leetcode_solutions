# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        pointer1 = list1
        pointer2 = list2
        current = None
        while pointer1 or pointer2:
            selected = None
            if pointer1 and pointer2:
                if pointer1.val < pointer2.val:
                    selected = pointer1
                    pointer1 = pointer1.next
                else:
                    selected = pointer2
                    pointer2 = pointer2.next
            elif not pointer1:
                selected = pointer2
                pointer2 = pointer2.next
            else:
                selected = pointer1
                pointer1 = pointer1.next
            if current:
                current.next = selected
                current = current.next
            else:
                current = selected
            if not head:
                head = current
        return head
        