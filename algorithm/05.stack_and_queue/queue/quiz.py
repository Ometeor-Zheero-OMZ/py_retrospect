from collections import deque

def reverse(queue: deque) -> None:
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())

    return [queue.append(d) for d in new_queue] 

if __name__ == "__main__":
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    reverse(q)
    print(q)