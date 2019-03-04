from typing import Dict, Tuple, Sequence, Any, NoReturn, Optional


class Node():
    def __init__(self,
                 val: Any,
                 next_node=None):
        self.val = val
        self.next_node = next_node


class SingleLinkedList():
    def __init__(self):
        self.head: Optional[Node] = None

    def empty(self) -> bool:
        """
        Specifies whether the linked list is empty
        """
        return self.head is None

    def push_front(self, val: Any) -> NoReturn:
        """
        Add new Node to the front of the LinkedList
        Run time complexity of O(1)
        """
        if self.empty():
            self.head = Node(val)
        else:
            self.head = Node(val, self.head.next_node)

    def get_front(self) -> Any:
        """
        Return the first Node of the LinkedList
        Run time complexity of O(1)
        """
        if self.empty:
            return None
        else:
            return self.head.val

    def pop_front(self) -> Node:
        """
        Remove first Node from the LinkedList and return it
        Run time complexity of O(1)
        """
        if self.empty:
            raise Exception('LinkedList is empty, unable to pop_front')
        else:
            self.head = self.head.next_node

    def push_back(self, key) -> NoReturn:
        """
        Add new node to the end of the linked list
        """
        node = self.head

        while node.next_node is not None:
            node = node.next_node

        new_node = Node(key)
        node.next_node = new_node

    def get_back(self) -> Any:
        """
        Returns the value of the last node in the linked list
        """
        if self.empty():
            return None
        node = self.head

        while node.next_node is not None:
            node = node.next_node

        return node.val

    def pop_back(self) -> Any:
        """
        Removes and returns the last node in the linked list
        """
        if self.empty():
            return None
        node = self.head
        prev_node = None

        while node.next_node is not None:
            prev_node = node
            node = node.next_node

        prev_node.next_node = None
        return node.val

    def insert_before(self, target_node: Node, key: Any) -> Any:
        """
        Create and insert node before specified node
        """
        if self.empty():
            raise Exception('Linked list is empty, unable to insert node')

        current_node = self.head
        prev_node = None

        while current_node.next_node is not None:
            prev_node = current_node
            if current_node == target_node:
                current_node = current_node.next_node
