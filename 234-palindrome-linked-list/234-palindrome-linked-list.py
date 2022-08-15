# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        '''
        1. find first half of LL
        2. reverse second half of LL
        3. compare each value
        4. reverse second half of LL
        '''
        # edge case: head is one or zero nodes
        if not head or not head.next:
            return True
        
        # find first half of L
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse the second half of next and keep a pointer to the start of it
        reversed_head = self.reverse(slow)
        # reversed_head_copy = reversed_head
        
        while head and reversed_head:
            if head.val != reversed_head.val:
                break
            head = head.next
            reversed_head = reversed_head.next
            
        # I've reached the end
        # self.reverse(reversed_head_copy)
        if slow is None or reversed_head is None:
            return True
        return False
    
    def reverse(self, head: Optional[ListNode]) -> ListNode:
        prev = None
        while (head is not None):
            # swap pointers
            head.next, prev, head = prev, head, head.next
        return prev