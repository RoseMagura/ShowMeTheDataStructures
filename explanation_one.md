# Problem One Explanation

I used a dictionary to store the values at their corresponding indices
to make storing and retrieving them easier and more efficent. Then,
I utilized a linked list to help keep track of the order that the 
elements were used in. The linked list can be used more efficiently
than a normal list or queue in this case.

The time efficiency for this solution is O(1), because the program just
directly accesses parts of the dictionary by index or the tail
of the linked list. No loops or sorting is involved, which keeps things 
simple. 

Space Complexity: Just storing a small quantity of variables in a dictionary
and linked list will keep things simple and compact. 