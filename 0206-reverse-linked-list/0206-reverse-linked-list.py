class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:

            nxt = curr.next      # Save next node

            curr.next = prev     # Reverse pointer

            prev = curr          # Move prev

            curr = nxt           # Move curr

        return prev