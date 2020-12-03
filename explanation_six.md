# Problem Six Explanation

For the function that finds the union of two linked lists, I created a set
which will store the values of all of the nodes in both. By looping through
both linked lists, I was able to easily get the values and store them 
quickly in the set. The order doesn't really matter and only one 
instance of each value should be stored, so a set works best for this case.

For the function that finds the intersection of the two linked lists, 
I also used sets to keep things simple. I stored the values from each linked
list separately and then iterated through one while checking if the value
was also found in the other set. If it was in both, I appended it to the 
intersection linked list. Checking if a value is in a set has an average
time complexity of O(1) and a worst case of O(n). For a list, the average
case is O(n), making checking the sets more time efficient. 

Sets do take up more space than lists in the memory, so that is less 
efficient. However, these sets are very small and shouldn't cause any
problems.