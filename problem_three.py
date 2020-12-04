import sys, collections
from heapq import heapify, heappush, heappop

class Node:
    def __init__(self, value, char = None, parent = None, left_sibling = None):
        self.char = char
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.left_sibling = None
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
    
    def is_leaf(self):
        if self.right == None and self.left == None:
            return True
        else:
            return False

    def __repr__(self):
        return f"Node({self.get_value()}{self.char})"

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

# def create_heap(data):
#     heap = []
#     heapify(heap)
#     for key, value in data.items():
#         heappush(heap, (key, value))
#     return heap

class Tree():
    def __init__(self, node):
        self.root = node
        
    def set_root(self,value):
        self.root = Node(value)
        
    def get_root(self):
        return self.root
    
    def traverse(self, node, combined=[]):
        if node:
            combined.append(node)
            self.traverse(node.get_left_child(), combined)
            self.traverse(node.get_right_child(), combined)
        return combined
    
    def find_leaves(self):
        node = self.get_root()
        leaves = list()
        all = self.traverse(node, [])
        for item in all:
            if item.is_leaf():
                leaves.append(item)  
        return leaves

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

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level        
        return s

def sort_list(list):
    return sorted(list, key = lambda x: x.value)

def calculate_code(cur_node, root, code=[]):
    if cur_node == root:
        return
    else:
        if cur_node.left_sibling:
            code.append(0)
        else:
            code.append(1)
        calculate_code(cur_node.parent, root, code)
    code = code[::-1]
    code = str(code).strip('[]')
    code = code.split(', ')
    code = ''.join(code)
    return code

def huffman_encoding(data):
    chars = find_char_freq(data)
    # heap = create_heap(chars)
    priority_queue = list()
    for key, value in chars.items():
        priority_queue.append(Node(value, key))
    priority_queue = sort_list(priority_queue)

    while len(priority_queue) > 1:
        min1 = priority_queue[0]
        min2 = priority_queue[1]
        sum = min1.value + min2.value
        new_node = Node(sum)
        new_node.set_left_child(min1)
        new_node.set_right_child(min2)
        min1.parent = new_node
        min1.left_sibling = True
        min2.left_sibling = False
        min2.parent = new_node
        priority_queue.append(new_node)
        priority_queue = priority_queue[2:]
        priority_queue = sort_list(priority_queue)
    tree = Tree(priority_queue[0])
    node = tree.get_root()
    codes = dict()
 
    leaves = tree.find_leaves()
    # for leaf in leaves:
    #     string = str(calculate_code(leaf, node, []))
    #     codes[leaf.char] = string
    # print(codes)
    # final_string = ''
    # for d in data:
    #     final_string += codes.get(d, '')
    # return final_string, tree
    return

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "BCAADDDCCACACAC"

    huffman_encoding(a_great_sentence)
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))