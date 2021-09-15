import random


class Node(object):
    """binary search tree implemented by linked list"""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree(object):
    """
    support search, min, max, successor, insert, delete, random_build in O(h), h is height of tree
    """

    def __init__(self, root=None):
        self.root = root

    def inorder_traversal(self, node: Node):
        """
        time O(n)
        """
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key)
            self.inorder_traversal(node.right)

    def search(self, key):
        node = self.root
        while node is not None and node.key != key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node

    @staticmethod
    def min(node: Node):
        """find min in subtree"""
        while node is not None:
            node = node.left
        return node

    @staticmethod
    def max(node: Node):
        """find max in subtree"""
        while node is not None:
            node = node.right
        return node

    def successor(self, node: Node):
        """
        successor of node is the node with the smallest key > node.key
        work on distinct and non distinct key
        """
        # case 1: successor is min in right subtree
        while node.right is not None:
            return self.min(node.right)
        # case 2: successor is parent node
        parent_node = node.parent
        while parent_node is not None and node == parent_node.right:
            # go up
            node = parent_node
            parent_node = parent_node.parent
        return parent_node

    def insert(self, key):
        parent_node = None
        new = Node(key)
        node = self.root
        # find correct leaf to insert new node
        while node is not None:
            # set current node as parent node
            parent_node = node
            # current node goes left
            if new.key < node.key:
                node = node.left
            # current node goes right
            else:
                node = node.right
        new.parent = parent_node
        # case 1: empty tree
        if parent_node is None:
            self.root = new
        # case 2: new node is parent_node.left
        elif new.key < parent_node.key:
            parent_node.left = new
        # case 3: new node is parent_node.right
        else:
            parent_node.right = new
        return new

    def delete(self, node: Node) -> None:
        # case 1: node has no left child, replace node with its right child, which can be None
        if node.left is None:
            self.transplant(node, node.right)
        # case 2: node has no right child, replace node with its left child
        elif node.right is None:
            self.transplant(node, node.left)
        # case 3:
        # node has 2 children

        else:
            # find successor_node, which lie in node's right subtree and has no left child
            node_successor = self.min(node.right)
            # case 3.1: successor_node is not node's right child, do some extra work
            if node_successor.parent != node:
                self.transplant(node_successor, node_successor.right)
                # connect node_successor and subtree rooted at node.right
                node_successor.right = node.right
                node_successor.right.parent = node_successor
            # case 3.2:
            # if node_successor is node's right subtree, replace node by node_successor
            self.transplant(node, node_successor)
            # connect node's left subtree to node_successor
            node_successor.left = node.left
            node_successor.left.parent = node_successor

    def transplant(self, deleted_subtree_root: Node, inserted_subtree_root: Node) -> None:
        """
        move subtree around within binary search tree
        replace the subtree rooted at node inserted_subtree_root with the subtree rooted at node deleted_subtree_root
        time: O(1)
        """
        # deleted_subtree_root is root of tree
        if deleted_subtree_root.parent is None:
            self.root = inserted_subtree_root
        # deleted_subtree_root is left subtree of parent, insert to parent.left to replace it
        elif deleted_subtree_root == deleted_subtree_root.parent.left:
            deleted_subtree_root.parent.left = inserted_subtree_root
        # deleted_subtree_root is right subtree of parent, insert to parent.right to replace it
        else:
            deleted_subtree_root.parent.right = inserted_subtree_root
        # update inserted_subtree_root.parent
        if inserted_subtree_root is not None:
            inserted_subtree_root.parent = deleted_subtree_root.parent

    def random_build(self, keys: list):
        """build binary search tree with random keys, so the expected height of the tree will be lg(n)"""
        random.shuffle(keys)
        for i in keys:
            self.insert(keys[i])
