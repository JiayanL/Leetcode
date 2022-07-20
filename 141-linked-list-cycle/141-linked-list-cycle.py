# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # hash table method
        
        nodes_seen = set()
        while head:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False