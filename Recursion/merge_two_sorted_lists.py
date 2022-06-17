class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            next_node = self.mergeTwoLists(l1.next, l2)
            l1.next = next_node
            return l1
            
        else:
            next_node = self.mergeTwoLists(l1, l2.next)
            l2.next = next_node
            return l2