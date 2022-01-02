class SinglyNode(object):

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return self.data


class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    # get length
    # time O(n)
    # space O(1)
    def __len__(self):
        curr = self.head
        length: int = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    # time O(n)
    # space O(n)
    def to_array(self):
        return_arr = []
        curr = self.head
        while curr is not None:
            return_arr.append(curr.data)
            curr = curr.next
        return return_arr

    # time O(1)
    # space O(1)
    def insert_to_front(self, data) -> SinglyNode:
        node = SinglyNode(data, self.head)
        self.head = node
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
        return node

    # time O(n)
    # space O(1)
    def search_list(self, key) -> SinglyNode:
        curr = self.head
        while curr is not None and curr.data != key:
            curr = curr.next
        return curr

    def delete_node(self, data) -> any:
        # case 0: empty list
        if self.head is None:
            return None
        # case 1: has 1 element
        curr = self.head
        if curr.data == data:
            self.head = curr.next
            return curr
        # case 2: has more than 1 elements
        while curr.next is not None:
            if curr.next.data == data:
                curr.next = curr.next.next
                return curr
            curr = curr.next
        return None


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

    # get length
    # time O(1)
    # space O(1)
    def __len__(self):
        curr = self.head
        length: int = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    # time O(n)
    # space O(n)
    def to_array(self):
        return_arr = []
        curr = self.head
        while curr is not None:
            return_arr.append(curr.data)
            curr = curr.next
        return return_arr

    # time O(1)
    # space O(1)
    def insert_to_front(self, data):
        node = DoublyNode(data, None, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        return node

    # insert to rear
    # time O(n) if we have rear pointer, we can achieve O(1)
    # space O(1)
    def append(self, data):
        # case 1: empty list
        if self.head is None:
            node = DoublyNode(data, None, self.head)
            self.head = node
            return node
        # case 2: non empty list
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        node = DoublyNode(data, curr_node, None)
        curr_node.next = node
        return node

    # time O(n)
    # space O(1)
    def search_list(self, key):
        curr = self.head
        while curr is not None and curr.data != key:
            curr = curr.next
        return curr

    # time O(n)
    # space O(1) not ok
    def delete_node(self, data) -> any:
        # case 0: empty list
        if self.head is None:
            return None
        # case 1: has 1 element

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return self.head
        # case 2: has more than 1 elements
        curr = self.head.next
        while curr is not None:
            if curr.data == data:
                curr.prev.next = curr.next
                if curr.next is not None:  # curr is not the last element
                    curr.next.prev = curr.prev
                return curr
            curr = curr.next
