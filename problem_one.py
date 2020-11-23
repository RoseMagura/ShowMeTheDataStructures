class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        self.size += 1
        node = DoubleNode(value)
        if self.size > 5:
            self.remove(self.tail.value)
        if self.head is None:
            self.head = node
            self.tail = self.head
            return
        temp = self.head
        temp.prev = node
        node.next = temp
        self.head = node
        return
    
    def remove(self, value):
        self.size -= 1
        if value == self.tail.value:
            to_be_deleted = self.tail
        else:
            node = self.head
            while node:
                if node.value == value:
                    to_be_deleted = node
                    return
                node = node.next
        print('deleting', str(value))
        to_be_deleted.prev.next = None
        self.tail = self.tail.prev
        self.size -= 1
        return to_be_deleted.value
    
    def __repr__(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.elements = dict()
        self.capacity = capacity
        self.size = 0
        self.order = DoublyLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        item = self.elements.get(key, -1)
        if item > -1:
            self.order.remove(key)
            self.order.append(key)
        return item

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item. 
        if self.size >= self.capacity:
            # remove item
            deleting = self.order.remove(self.order.tail.value)
            del self.elements[deleting]
            # change capacity
            self.size -= 1
        if self.elements.get(key) == None:
            self.elements[key] = value
            self.size += 1
            self.order.append(value)
        return
    
    def __repr__(self):
        return str(self.elements)

our_cache = LRU_Cache(5)

our_cache.set(1, 1);

our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)       # returns 1

our_cache.get(2)       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print('order of elements')
our_cache.order.__repr__()

print(our_cache.get(3))   # returns -1 because the cache reached its capacity and 3 was the least recently used entry