import pytest

from linked_list import *


class TestLinkedList:
    def test_insert(self):
        linked_list = LinkedList(None)
        linked_list.insert_to_front(0)
        linked_list.append(4)
        linked_list.append(2)
        linked_list.insert_to_front(3)
        assert linked_list.__len__() == 4