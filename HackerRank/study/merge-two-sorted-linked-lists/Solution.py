# reference
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

# solution
def mergeLists(head1, head2):
    all_node =[]
    
    cur_node = head1
    while cur_node:
        all_node.append(cur_node.data)
        cur_node = cur_node.next
    
    cur_node = head2
    while cur_node:
        all_node.append(cur_node.data)
        cur_node = cur_node.next
    
    all_node.sort(reverse=True)
    
    next_node = None
    for i in range(len(all_node)):
        node = SinglyLinkedListNode(all_node[i])
        node.next = next_node
        next_node = node

    return next_node