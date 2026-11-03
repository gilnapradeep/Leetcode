"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        dic = {}
        current = head

        while current:
            dic[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            dic[current].next = dic.get(current.next)
            dic[current].random = dic.get(current.random)
            current = current.next

        return dic[head]
        