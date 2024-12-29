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
        """
        ノードを作成するコンストラクタ
        data: ノードのデータ
        next_node: 次のノードへの参照
        """
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self, head = None) -> None:
        """
        単方向リストの初期化
        head: リストの最初のノードへの参照
        """
        self.head = head

    def append(self, data: Any) -> None:
        """
        リストの末尾に新しいノードを追加するメソッド
        data: 新しいノードに挿入するデータ
        """
        new_node = Node(data) # 新しいノードを作成

        # もしリストが空なら、head が None の場合、新しいノードがリストの最初になる
        if self.head is None:
            self.head = new_node
            return
        
        # リストが空でない場合、最後のノードを探して新しいノードを追加する
        tail_node = self.head
        while tail_node.next: # 次のノードがある限り、次に進む
            tail_node = tail_node.next

        # 最後のノードの next に新しいノードを設定
        tail_node.next = new_node

    def insert(self, data: Any) -> None:
        """
        リストの先頭に新しいノードを挿入するメソッド
        data: 新しいノードに挿入するデータ
        """
        new_node = Node(data) # 新しいノードを作成
        new_node.next = self.head # 新しいノードの次に元の head を設定
        self.head = new_node # head を新しいノードに更新

    def print(self) -> None:
        """
        リストの全ノードのデータを順番に表示するメソッド
        """
        curr_node = self.head # 現在のノードは head から始める

        while curr_node: # ノードがなくなるまで繰り返す
            print(curr_node.data) # ノードのデータを表示
            curr_node = curr_node.next # 次のノードに進む

    def remove(self, data: Any) -> None:
        """
        指定したデータを持つノードをリストから削除するメソッド
        data: 削除したいノードのデータ
        """
        curr_node = self.head # 現在のノードは head から始める

        # もし head が削除対象であれば、head を次のノードに更新
        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node = None # メモリを解放
            return

        prev_node = None # 前のノード
        while curr_node and curr_node.data != data:
            prev_node = curr_node # 現在のノードを前のノードにセット
            curr_node = curr_node.next # 次のノードに進む

        if curr_node is None: # 削除するノードが見つからなかった場合
            return

        # 削除するノードの前のノードが、削除するノードの次を指すようにする
        prev_node.next = curr_node.next
        curr_node = None # メモリ解放

    def reverse_iterative(self) -> None:
        """
        リストを反転させる（反復法）メソッド
        全てのノードの次を逆順に変更して、head を更新する
        """
        prev_node = None # 反転前のノード
        curr_node = self.head # 現在のノードは head から始める

        while curr_node: # ノードがある限り繰り返す
            next_node = curr_node.next # 次のノードを保存
            curr_node.next = prev_node # 現在のノードの次を前のノードに設定
            prev_node = curr_node # 前のノードを更新
            curr_node = next_node # 現在のノードを次のノードに更新

        self.head = prev_node # 最後に前のノードが head となる

    def reverse_recursive(self) -> None:
        """
        リストを反転させる (再帰法) メソッド
        再帰敵にリストの反転を行い、最終的に head を更新する
        """
        def _reverse_recursive(curr_node: Node, prev_node: Node) -> Node:
            if not curr_node: # 現在のノードが None の場合、前のノードが新しい head
                return prev_node

            next_node = curr_node.next # 次のノードを保存
            curr_node.next = prev_node # 現在のノードの次を前のノードに設定
            prev_node = curr_node # 前のノードを更新
            curr_node = next_node # 現在のノードを次のノードに更新
            return _reverse_recursive(curr_node, prev_node) # 再帰的に呼び出す

        self.head = _reverse_recursive(self.head, None) # 最初に呼び出す

if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(2)
    l.append(3)
    l.insert(0)
    l.print()

    print("###############")
    l.reverse_iterative()
    l.print()

    print("###############")
    l.reverse_recursive()
    l.print()

    print("###############")
    l.remove(2)
    l.print()