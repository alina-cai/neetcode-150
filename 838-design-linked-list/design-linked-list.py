class ListNode:

    def __init__(self, val, prev = None, next = None):
        self.prev = prev
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def get(self, index: int) -> int:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            return cur.val

        return -1
        

    def addAtHead(self, val: int) -> None:
        prev, node, next = self.left, ListNode(val), self.left.next
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
        

    def addAtTail(self, val: int) -> None:
        prev, node, next = self.right.prev, ListNode(val), self.right
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and index == 0:
            prev, node = cur.prev, ListNode(val)
            node.next = cur
            node.prev = prev
            prev.next = node
            cur.prev = node


    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next

        while cur and index > 0:
            cur = cur.next
            index -= 1

        if cur and cur != self.right and index == 0:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

# time: O(n)
# space: O(1)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)