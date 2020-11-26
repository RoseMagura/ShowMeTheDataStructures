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

class Tree(object):
    def __init__(self, value):
        self.root = Node(value)
        # nodes = nodes[:-3]
        # current_node = self.root.get_right_child()
        # while len(nodes) > 1:
        #     print (nodes[-1])
        #     print(nodes[-2])
        #     current_node.set_right_child(nodes[-1])
        #     current_node.set_left_child(nodes[-2])
        #     current_node = current_node.get_right_child()
        #     nodes = nodes[:-2]
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

def huffman_encoding(data):
    chars = find_char_freq(data)
    key_list = list(chars.keys())
    value_list = list(chars.values())
    heap = create_heap(chars)
    # print(chars)
    node_values = []
    parents = []

    tree = Tree(sum(value_list))
    # tree.insert(Node(10))
    # tree.insert(Node(19))
    # tree.insert(Node(18))

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
        parent = Node(new_value)
        parent.set_left_child(node1)
        parent.set_right_child(node2)
        node_values.append(new_value)
        parents.append(parent)

        # tree.insert(parent)

        # add back to heap
        heappush(heap, new_value)

    current_node = tree.get_root()
    while current_node:
        for p in parents[::-1]:
            if current_node is None:
                break
            print('current value', str(current_node.value))
            print(current_node.value == p.value)
            if p.value == current_node.value:
                current_node.set_left_child(p.get_left_child())
                current_node.set_right_child(p.get_right_child())
            print(current_node.get_left_child())
            current_node = current_node.get_right_child()
            
    # current_node = tree.get_root()
    # while current_node:
    #     for p in parents[::-1]:
    #         if current_node is None:
    #             break
    #         print('current value', str(current_node.value))
    #         print(current_node.value == p.value)
    #         if p.value == current_node.value:
    #             current_node.set_left_child(p.get_left_child())
    #             current_node.set_right_child(p.get_right_child())
    #         current_node = current_node.get_left_child()  
    print(tree.__repr__())
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