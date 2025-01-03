"""
Queue
In computer science, a queue is a particular kind of abstract data type or collection in which the entities in the collection 
are kept in order and the principal (or only) operations on the collection are the addition of entities to the rear terminal position,
known as enqueue, and removal of entities from the front termianl position, known as dequeue.
This makes the queue a First-In-First-Out (FIFO) data structure. In a FIFO data structure, the first element added to the queue will be the first one to be removed.
This is equivalent to the requirement that once a new element is added, all elements that were added before have to be removed before the new element can be removed.
Often a peek or front operation is also entered, returning the value of the front element without dequeuing it.
A queue is an example of a linear data structure, or more abstractly a sequential collection.

"""

from typing import Any

class Queue:
    def __init__(self) -> None:
        self.queue = [] # queue に空の配列を用意

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)
        
if __name__ == "__main__":
    queue = Queue()

    print(queue.queue)
    queue.enqueue(1)
    print(queue.queue)
    queue.enqueue(2)
    print(queue.queue)
    print(queue.queue)
    queue.enqueue(3)
    print(queue.queue)
    queue.enqueue(4)
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)
    queue.dequeue()
    print(queue.queue)