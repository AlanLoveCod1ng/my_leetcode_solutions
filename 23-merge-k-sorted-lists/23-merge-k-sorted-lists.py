# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i in range(len(lists)):
            #[value, index_of_list, index_of_value]
            if lists[i] == None:
                continue
            heapq.heappush(heap, Value_Node(lists[i]))
        head = None
        tail = head
        while len(heap) != 0:
            current = heapq.heappop(heap)
            val = current.val
            node = current.node
            if head == None:
                head = node
            if tail == None:
                tail = node
            else:
                tail.next = node
                tail = tail.next
            next_node = node.next
            if next_node:
                heapq.heappush(heap, Value_Node(next_node))
        return head
    
class Value_Node:
    def __init__(self,node):
        self.val = node.val
        self.node = node
    def __lt__(self,other):
        return self.val<other.val