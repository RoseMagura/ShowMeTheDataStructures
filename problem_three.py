import sys, collections
from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, value, char = None):
        self.char = char
        self.value = value
        self.left = None
        self.right = None
# add set_value and get_value functions
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

    def __repr__(self):
        return f"Node({self.get_value()})"

class Queue():
    def __init__(self):
        self.q = collections.deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def empty(self):
        return self.__len__() == 0

class Tree(object):
    def __init__(self, value):
        # self.root = Node(value)
        self.root = value

    def get_root(self):
        return self.root
        
    def insert(self, node):
        print('inserting', str(node.value))
        current_node = self.root
        while current_node:
            print(current_node.value)
            if node.value == current_node.value:
                print('equal')
                return
            elif node.value > current_node.value:
                print('greater')
                if current_node.has_right_child():
                    current_node = current_node.get_right_child()
                else:
                    current_node.set_right_child(node)
                    return
            elif node.value < current_node.value:
                print('less')
                if current_node.has_left_child():
                    if node.value > current_node.get_left_child().value:
                        print('greater than left child')
                        temp = current_node.get_left_child()
                        current_node.set_left_child(node)
                        node.set_left_child(temp)
                        return
                        if current_node.has_right_child():
                            current_node = current_node.get_right_child()
                        else:
                            current_node.set_right_child(node)
                            return
                    
                    current_node = current_node.get_left_child()
                else:
                    current_node.set_left_child(node)
                    return
            else:
                return None
        
        else:
            return None


    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "\nTree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level          
        return s

def find_char_freq(string):
    return collections.Counter(string)

def create_heap(data):
    heap = []
    heapify(heap)
    for value in data.values():
        heappush(heap, value)
    return heap

def create_tree(arr):
    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None
    
    root = Node(arr[index])
    index += 1
    queue = Queue()
    queue.enq(root)

    while not queue.empty() and index < length:
        current_node = queue.deq()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = Node(left_child)
            current_node.left = left_node
            queue.enq(left_node)
        
        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = Node(right_child)
            current_node.right = right_node
            queue.enq(right_node)
    return root

def huffman_encoding(data):
    chars = find_char_freq(data)
    key_list = list(chars.keys())
    value_list = list(chars.values())
    heap = create_heap(chars)
   
    node_values = []
    # parents = []

    # tree = Tree(sum(value_list))

    while len(heap) > 1:
        min1 = heappop(heap)

        node1 = Node(min1
        # , chars.get(value_list.index(min1),)
        )
        # print(key_list[value_list.index(min1)])
        min2 = heappop(heap)

        node2 = Node(min2
        # , chars[min2]
        )
        # merge those two 
        new_value = min1 + min2
       
        # parent = Node(new_value)
        # parent.set_left_child(node1)
        # parent.set_right_child(node2)
       
        node_values.append(new_value)
       
        # add back to heap
        heappush(heap, new_value) 

    root = create_tree(node_values[::-1])

    left1 = root.get_left_child()
    right1 = root.get_right_child()
    print('left1', left1)
    print('right1', right1)

    left2 = left1.get_left_child()
    print('left2', left2)
    right2 = left1.get_right_child()
    print('right2', right2)
    print(left2.get_left_child())
    print(left2.get_right_child())

    print(right1.get_left_child())
    print(right1.get_right_child())
    return

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    huffman_encoding(a_great_sentence)
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))