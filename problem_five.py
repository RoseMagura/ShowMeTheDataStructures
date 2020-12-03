import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        sha.update(self.data.encode('utf-8'))

        return sha.hexdigest()
    
    def __repr__(self):
        return str(self.timestamp) + ' | ' + str(self.data) \
            + ' | ' + str(self.previous_hash) + ' | ' \
            + str(self.hash)

class BlockChain(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def appendBlock(self, data):
        if data is None or data == '':
            return
        elif self.head is None:
            self.head = Block(datetime.utcnow(), data, 0)
            self.tail = self.head
        else:        
            self.tail.next = Block(datetime.utcnow(), data, self.tail.hash)
            self.tail = self.tail.next
        return
            
    def __repr__(self):
        output = []
        block = self.head
        while block:
            output.append([block])
            block = block.next
        return output

blockchain = BlockChain()
blockchain.appendBlock('abc')
blockchain.appendBlock('def')
blockchain.appendBlock('ghi')
print(blockchain.__repr__()) # prints block chain with three blocks

bc = BlockChain()
bc.appendBlock('123')
bc.appendBlock(None)
print(bc.__repr__()) # prints block chain with only one block

bc2 = BlockChain()
bc2.appendBlock('')
bc2.appendBlock('')
print(bc2.__repr__()) # prints empty block chain
