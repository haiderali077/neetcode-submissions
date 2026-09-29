"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copyofNodes = {None : None}

        curr = head

        while curr:
            copy = Node(curr.val)
            copyofNodes[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = copyofNodes[curr]
            copy.next = copyofNodes[curr.next]
            copy.random = copyofNodes[curr.random]
            curr = curr.next

        return copyofNodes[head]
        