class SinglyNode(object):

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return self.data


class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.len = 0

    # get length
    # time O(1)
    # space O(1)
    def __len__(self):
        return self.len

    # time O(1)
    # space O(1)
    def insert_to_front(self, data) -> SinglyNode:
        node = SinglyNode(data, self.head)
        self.head = node
        self.len += 1
        return node

    # insert to rear
    # time O(n) if we have rear pointer, we can achieve O(1)
    # space O(1)
    def append(self, data) -> SinglyNode:
        node = SinglyNode(data, None)
        # case 1: empty list
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        self.len += 1
        return node

    # time O(n)
    # space O(1)
    def search_list(self, key) -> SinglyNode:
        curr = self.head
        while curr is not None and curr.data != key:
            curr = curr.next
        return curr

    # time O(n)
    # space O(1)
    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    # time O(n)
    # space O(1)
    def delete_node(self, data) -> any:
        # case 0: empty list
        if self.head is None:
            return None
        curr = self.head
        # case 1: has 1 element
        if curr.data == data:
            curr = curr.next
        # case 2: has more than 1 elements
        while curr is not None:
            if curr.next.data == data:
                curr.next = curr.next.next
                return curr
            curr = curr.next
        self.len -= 1
        return None  # add extra

    def delete_list(self) -> None:
        """mark it as deleted to garbage collector will take care of it"""
        del self.head


class DoublyNode(object):
    def __init__(self, data=0, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        return self.data


class DoublyLinkedList(object):
    def __init__(self, head):
        self.head = head
        self.len = 0

    # get length
    # time O(1)
    # space O(1)
    def __len__(self):
        return self.len

    # time O(1)
    # space O(1)
    def insert_to_front(self, data):
        node = DoublyNode(data, None, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        self.len += 1
        return node

    # insert to rear
    # time O(n) if we have rear pointer, we can achieve O(1)
    # space O(1)
    def append(self, data):
        node = SinglyNode(data, None)
        # case 1: empty list
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        self.len += 1
        return node

    # time O(n)
    # space O(1)
    def search_list(self, key):
        curr = self.head
        while curr is not None and curr.data != key:
            curr = curr.next
        return curr

    # time O(n)
    # space O(1)
    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    # time O(n)
    # space O(1)
    def delete_node(self, data):
        # case 0: empty list
        if self.head is None:
            return None
        curr = self.head
        # case 1: has 1 element
        if curr.data == data:
            curr = curr.next
        # case 2: has more than 1 elements
        while curr is not None:
            if curr.next.data == data:
                curr.next = curr.next.next
                return True  #
            curr = curr.next
        self.len -= 1
        return False  # add extra

    # time O(1)
    def delete_list(self):
        del self.head
