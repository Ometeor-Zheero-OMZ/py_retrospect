"""
Stack
In computer science, a stack is an abstract data type that serves as a collection of elements,
with two principal operations: push, which adds an element to the collection, and pop, which removes the most recently added element that was not yet removed.
The oreder in which elements come off a stack gives rise to its alternative name, LIFO (for last in, first out).
Additionally, a peek operation may give access to the top without modifying the stack.

"""

from typing import Any

class Stack:
    def __init__(self) -> None:
        self.stack = [] # stack に空の配列を用意

    def push(self, data) -> None:
        self.stack.append(data) # 配列の後ろから要素を追加

    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop() # 配列の後ろから要素を取り出す
        
if __name__ == "__main__":
    stack = Stack()

    print(stack.stack)
    stack.push(1)
    print(stack.stack)
    stack.push(2)
    print(stack.stack)
    stack.pop()
    print(stack.stack)
    stack.pop()
    print(stack.stack)