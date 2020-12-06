# Problem Three Explanation

I added some extra features to the Node class, such as a char field
to store the optional character for the node. Value corresponds to the 
number of times that character is found in the data string. I also 
added some fields about the node's parent (in the tree) and whether it 
is the left child/sibling or not. This helps me with keeping track of 
where the node is when determining the value of the code for each
character.

I used the collections module to easily create a dictionary for each 
character's frequency in the input string. 

For keeping track of the leaves, I used a list, since they take up 
less space compared to a set and are easy to iterate over. I also used a
list instead of a min heap when creating the tree with the values and 
characters from the data string. Even though sorting a list uses slightly
more time (n log n) than the min heap (just log n to push and pop), I chose
a list for better readability. Min heap doesn't allow you to use it with 
nodes and tuples, since it can't compare the values. I felt like it was 
easier and more streamlined to store tuples in the list (character and
frequency), convert them to nodes, store the nodes again, and then make
a tree with the final node. Using the min heap would have required more 
complicated functions to get the character for a frequency value, which
for me outweighed the time complexity. I only sort the list once at the 
beginning and once for each iteration of the loop, so it seemed like 
an okay compromise to make. 