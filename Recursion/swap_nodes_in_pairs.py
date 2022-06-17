class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        n1 = head
        n2 = head.next
        
        # point n1 to the next pairs after (n1, n2) pair
        n1.next = self.swapPairs(n2.next)
        n2.next = n1
        
        # because n2 is now earlier than n1
        return n2
