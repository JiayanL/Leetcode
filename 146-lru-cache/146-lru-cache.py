# Define node for doubly linked list
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        # Check if key is in dictionary
        if key in self.key_dict:
            node = self.key_dict[key]
            # remove node from LRU
            self._remove(node)
            # add node to LRU
            self._add(node)
            # return value of node
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        # check if cache is at capacity and node is not in dictionary
        if key in self.key_dict:
            self._remove(self.key_dict[key])
        # if so, remove the most recent and delete from dictionary
        node = Node(key, value)
        self._add(node)
        self.key_dict[key] = node
        if len(self.key_dict) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            self.key_dict.pop(lru.key)
        # remove node if its alraedy in LRU
        # add node to LRU
        # add node to dictionary
    
    def _add(self, node) -> None:
        # find the node before the tail
        last_node = self.tail.prev
        # set the next of that node to current node
        last_node.next = node
        # set the next of current node to tail
        node.next = self.tail
        # set the previous of current node to prevoius node
        self.tail.prev = node
        # set the previous of tail to current node
        node.prev = last_node
    
    def _remove(self, node) -> None:
        # set the previous node's next to current node's next
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)