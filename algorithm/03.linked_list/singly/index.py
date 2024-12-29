"""
Singly linked list
In computer science, a linked list is a linear collection of data elements, in which linear order is not given by their physical placement in memeory.
Instead, each element points to the next. It is a data structure consisting of a group of nodes which together represent a sequence. 
Under the simplest form,
each node is composed of data and a reference (in otehr words, link) to the next node in the sequence.
This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration.
More complex variants add additional links, allowind efficient insertion or removal from arbitrary element references.
"""

from __future__ import annotations
from typing import Any

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
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def remove(self, data: Any) -> None:
        curr_node = self.head
        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node = None
            return

        prev_node = None
        while curr_node and curr_node.data != data:
            prev_node = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev_node.next = curr_node.next
        curr_node = None

if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.print()
    print("###############")
    l.remove(2)
    l.print()