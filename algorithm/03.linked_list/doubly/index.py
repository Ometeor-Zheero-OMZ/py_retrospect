from __future__ import annotations
from typing import Any, Optional

class Node:
    def __init__(self, data: Any, next_node: Node = None, prev_node: Node = None) -> None:
        self.data = data
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # リストの末尾を探す
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next

        # 新しいノードを末尾に追加
        curr_node.next = new_node
        new_node.prev = curr_node

    def insert(self, data: Any) -> Any:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        # 先頭に新しいノードを追加
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def print(self) -> None:
        curr_node = self.head

        while curr_node:
            print(curr_node.data) # 現在のデータを表示
            curr_node = curr_node.next # 次のノードに移動

    def remove(self, data: Any) -> Node:
        curr_node = self.head

        # 先頭ノードが削除対象の場合
        if curr_node and curr_node.data == data:
            if curr_node.next is None: # リストには1つのノードしかない場合
                curr_node = None
                self.head = None # リストを空にする
                return
            else:
                # 次のノードを新しい先頭に設定
                next_node = curr_node.next
                next_node.prev = None
                curr_node = None
                self.head = next_node
                return

        # 指定したデータを持つノードを探す
        while curr_node and curr_node.data != data:
            curr_node = curr_node.next

        # データが存在しない場合は終了
        if curr_node is None:
            return

        # 最後のノードの場合
        if curr_node.next is None:
            prev = curr_node.prev
            prev.next = None
            curr_node = None
            return
        else:
            # 削除対象のノードをスキップするようにリンクを更新
            next_node = curr_node.next
            prev_node = curr_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            curr_node = None
            return
        
    def reverse_iterative(self) -> None:
        prev_node = None
        curr_node = self.head
        
        while curr_node:
            # 現在のノードの prev と next を入れ替える
            prev_node = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = prev_node

            # 次のノードに進む (反転のためprev が次のノードになる)
            curr_node = curr_node.prev

        # リストの最後のノードが新しい先頭になる
        if prev_node:
            self.head = prev_node.prev

    def reverse_recursive(self) -> None:
        def _reverse_recursive(curr_node: Node) -> Optional[Node]:
            # 現在のノードが None の場合、処理を終了
            if not curr_node:
                return None
        
            # 現在のノードの prev と next を入れ替える
            prev_node = curr_node.prev
            curr_node.prev = curr_node.next
            curr_node.next = prev_node

            # 新しいヘッドに到達した場合、そのノードを返す
            if curr_node.prev is None: # prev が None の場合、現在のノードが新しいヘッドとなる
                return curr_node
            
            # 次のノードに進む (反転のためprev が次のノードになる)
            return _reverse_recursive(curr_node.prev)
        
        # リストのヘッドを更新
        self.head = _reverse_recursive(self.head)    

if __name__ == "__main__":
    d = DoublyLinkedList()
    d.append(0)
    d.append(1)
    d.append(2)
    d.append(3)
    d.insert(4)
    d.print()
    print("##################")
    d.remove(2)
    d.remove(4)
    d.print()

    print("##################")
    d.reverse_iterative()
    d.print()
    
    print("##################")
    d.reverse_recursive()
    d.print()