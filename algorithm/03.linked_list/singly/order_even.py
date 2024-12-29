from __future__ import annotations
from typing import Any, Optional

class Node:
    def __init__(self, data: Any, next_node: Node = None) -> None:
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        tail_node = self.head
        while tail_node.next:
            tail_node = tail_node.next

        tail_node.next = new_node

    def insert(self, data: Any) -> None:
        """
        リストの先頭に新しいノードを挿入するメソッド
        data: 新しいノードに挿入するデータ
        """
        new_node = Node(data) 
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        """
        リストの全ノードのデータを順番に表示するメソッド
        """
        curr_node = self.head

        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def reverse_even(self) -> None:
        def _reverse_even(head: Node, prev_node: Node) -> Optional[Node]:
            if head is None:
                return None
            
            curr_node = head
            while curr_node and curr_node.data % 2 == 0:
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node

            if curr_node != head:
                head.next = curr_node
                _reverse_even(curr_node, None)
                return prev_node
            else:
                head.next = _reverse_even(head.next, head)
                return head
        
        self.head = _reverse_even(self.head, None)

if __name__ == "__main__":
    l = LinkedList()

    arr = [1, 4, 6, 8, 9]

    for i in range(len(arr)):
        l.append(arr[i])

    l.print()
    print("################")
    l.reverse_even()
    l.print()

