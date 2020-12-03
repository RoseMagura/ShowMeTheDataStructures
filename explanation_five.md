# Problem Five Explanation

For this problem, I modified the normal Node class to include the necessary
blockchain concepts. The block is initialized with the current time,
found with datetime in a concise way, and other important information
like the hash. 

The Blockchain is implemented like a linked list in a simple way. Adding
a block is easy with the appendBlock method, which checks for edge cases
with the first if clause. Even if a user tries to add an empty block, the 
program will handle that input correctly. A new block is added as either
the head if no other blocks are present, or is added onto the tail. This
is a very time efficient solution, since it prevents looping and keeps 
the time efficiency at O(1). Linked lists are very compact in memory,
since the connected elements don't need to be stored side by side. 
Therefore, the Blockchain, which is like a linked list, is also easy to 
store efficiently. 