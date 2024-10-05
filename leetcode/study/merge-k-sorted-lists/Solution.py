from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for node in lists:
            while node:
                nodes.append(node.val)
                node = node.next
        
        # 큰 것부터 정렬
        nodes.sort(reverse=True)

        # 작은 노드의 next는 이전에 만든 node
        node = None
        for item in nodes:
            node = ListNode(item, node)
    
        return node
