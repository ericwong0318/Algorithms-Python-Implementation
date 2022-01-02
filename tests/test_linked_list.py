import unittest
from data_structure.linked_list import SinglyLinkedList, DoublyLinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.sll = SinglyLinkedList(None)
        self.dll = DoublyLinkedList(None)

    # singly linked list's test cases
    def test_singly_linked_list_insert_to_front(self):
        for i in reversed(range(10)):
            self.sll.insert_to_front(i)
        self.assertEqual([i for i in range(10)], self.sll.to_array())

    def test_singly_linked_list_append(self):
        for i in range(10):
            self.sll.append(i)
        self.assertEqual([i for i in range(10)], self.sll.to_array())

    def test_singly_linked_list_search_list(self):
        for i in range(10):
            self.sll.append(i)
        for i in range(10):
            self.assertEqual(i, self.sll.search_list(i).data)

    def test_singly_linked_list_delete_node(self):
        for i in range(9):
            self.sll.append(i)
        for i in range(9):
            if i % 2 == 0:
                self.sll.delete_node(i)
        self.assertEqual([j for j in range(9) if j % 2 != 0], self.sll.to_array())

    # doubly linked list's test cases
    def print_list_in_revered(self):
        """print list by node.prev for testing"""
        nodes = []
        curr = self.dll.head
        while curr.next is not None:
            curr = curr.next
        while curr is not None:
            nodes.append(curr.data)
            curr = curr.prev
        return nodes

    def test_doubly_linked_list_insert_to_front(self):
        for i in reversed(range(10)):
            self.dll.insert_to_front(i)
        self.assertEqual([i for i in range(10)], self.dll.to_array())
        self.assertEqual([i for i in reversed(range(10))], self.print_list_in_revered())

    def test_doubly_linked_list_append(self):
        for i in range(10):
            self.dll.append(i)
        self.assertEqual([i for i in range(10)], self.dll.to_array())
        self.assertEqual([i for i in reversed(range(10))], self.print_list_in_revered())

    def test_doubly_linked_list_search_list(self):
        for i in range(10):
            self.dll.append(i)
        for i in range(10):
            self.assertEqual(i, self.dll.search_list(i).data)

    def test_doubly_linked_list_delete_node(self):
        for i in range(9):
            self.dll.append(i)
        for i in range(9):
            if i % 2 == 0:
                self.dll.delete_node(i)
        self.assertEqual([j for j in range(9) if j % 2 != 0], self.dll.to_array())
        self.assertEqual([j for j in reversed(range(9)) if j % 2 != 0], self.print_list_in_revered())


if __name__ == '__main__':
    unittest.main()
