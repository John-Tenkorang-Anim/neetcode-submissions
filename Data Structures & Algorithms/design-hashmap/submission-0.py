class LinkedList:
    def __init__(self,key,val):
        self.v = val
        self.k = key
        self.next = None

class MyHashMap:
    def __init__(self):
        self.hmap = LinkedList(-1,-1)
        self.keys = []
        
    def put(self, key: int, value: int) -> None:
        if not key in self.keys:
            self.keys.append(key)
            new_node = LinkedList(key, value)
            new_node.next = self.hmap.next
            self.hmap.next = new_node
        else:
            curr = self.hmap
            while curr:
                if curr.k == key:
                    curr.v = value
                curr = curr.next

    def get(self, key: int) -> int:
        if not key in self.keys:
            return -1
        curr = self.hmap
        while curr:
            if curr.k == key:
                return curr.v
            curr = curr.next
        return -1
        
    def remove(self, key: int) -> None:
        if key in self.keys:
            self.keys.remove(key)
            prev = self.hmap
            curr = prev.next
            while curr:
                if curr.k == key:
                    prev.next = curr.next
                    break
                prev = curr
                curr = curr.next