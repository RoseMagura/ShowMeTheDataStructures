# Problem Four Explanation

For this problem, I used recursion to keep the code simple and readable.
The base case is checking if the target user is in the group's users. If
it is, then the function returns true and exits out of the cycle. Otherwise,
it will iterate through the groups and check those ones. The for loop
and checking for the string in the list of users have a combined time
complexity of O(n) for the worst case, which is not bad. Using a small
list of the users for each group doesn't take up a lot of space in the
memory, either, so this program can run quickly and efficiently. 