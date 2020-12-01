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
    
    root = arr[index]
    index += 1
    queue = Queue()
    queue.enq(root)

    while not queue.empty() and index < length:
        current_node = queue.deq()
        if current_node.char is not None:
            print(str(current_node), 'not getting children')
            index += 1
        else:
            right_child = arr[index]
            print(str(current_node), 'is getting right child of', str(right_child))
            index += 1

            if right_child is not None:
                current_node.right = right_child
                queue.enq(right_child)
            left_child = arr[index]
            index += 1

            if left_child is not None:
                print(str(current_node), 'is getting left child of', str(left_child))

                current_node.left = left_child
                queue.enq(left_child)
    return root

def get_key(val, d):
        for key, value in d.items():
            if val == value:
                return key

def print_tree(root):
    level = 0
    q = Queue()
    visit_order = list()
    node = root
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

def huffman_encoding(data):
    chars = find_char_freq(data)
    heap = create_heap(chars)
    leaves = []
    prev = None
    key_list = list(chars.keys())
    value_list = list(chars.values())
    value_list = sorted(value_list, reverse=True)
    node_values = []

    while len(heap) > 1:
        min1 = heappop(heap)

        node1 = Node(min1)
        min2 = heappop(heap)

        node2 = Node(min2)
        # merge those two 
        new_value = min1 + min2
       
        node_values.append(Node(new_value))
       
        for value in value_list:
            if value == new_value:
                c = get_key(value, chars)
                if c is not None:
                    node_values.append(Node(value, c))
                    del chars[c]
        # add back to heap
        heappush(heap, new_value) 

    node_values = node_values[::-1]
    for k, v in chars.items():
        node_values.append(Node(v, k))
    root = create_tree(node_values)
    # print(root.get_right_child().get_right_child().get_left_child())

    # print(root.get_right_child().get_right_child().get_left_child().get_left_child())
    # print(root.get_right_child().get_right_child().get_left_child().get_right_child())

    # print(print_tree(root))
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