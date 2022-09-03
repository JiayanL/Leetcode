# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # check for edge cases
        if left == right:
            return head
        
        current, previous = head, None
        # move all the way until I reach left
        i = 0
        while current is not None and i < left - 1:
            previous = current
            current = current.next
            i += 1
            
        last_node_in_sublist = current
        last_untouched_node = previous
        next = None
        # reverse left > right
        i = 0
        while current is not None and i < (right - left + 1):
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1
            
        # connect reversed portion
        if last_untouched_node is not None:
            # there's no next method
            last_untouched_node.next= previous
        else:
            head = previous
        
        last_node_in_sublist.next = current
        return head