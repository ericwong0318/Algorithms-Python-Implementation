from binary_search_tree import BinarySearchTree as Bst, Node as Node


def height(node) -> int:
    if node is None:
        return -1
    else:
        return node.height


def update_height(node) -> None:
    node.height = max(height(node.left), height(node.right)) + 1


class AvlTree(Bst):
    """Supports insert operations in O(lg n) time."""
    def __init__(self):
        super(AvlTree, self).__init__(Bst)

    def left_rotate(self, x):
        """
        x is root and y is x.right
        after left rotation, y will be the root and x will be y.left

        steps:
        1. y.left change to x.right
        2. x.parent change to y.parent
        3. x change to y.left
        4. update height of x, y
        """

        """step 1"""
        y = x.right  # set y as x's right child
        x.right = y.left  # turn y's left subtree (x < tree < y) into x's right subtree
        if y.left is not None:
            y.left.parent = x

        """step 2"""
        y.parent = x.parent  # link x's parent to y
        # change x's parent to y's parent
        # case 1: x is root
        if x.parent is None:
            self.root = y
        # case 2: x is left child of its parent
        elif x == x.parent.left:
            x.parent.left = y
        # case 3: x is right child of its parent
        else:
            x.parent.right = y

        """step 3"""
        y.left = x  # put x on y's left
        x.parent = y

        """step 4"""
        update_height(x)
        update_height(y)

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.parent.left == x:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

        update_height(x)
        update_height(y)

    def insert(self, key):
        """insert and modify it in-place."""
        node = Bst.insert(self, key)
        self.rebalance(node)

    def rebalance(self, node: Node):
        """check balance of tree and do rotation to fix its properties"""
        while node is not None:
            update_height(node)
            if height(node.left) > 1 + height(node.right):
                if height(node.left.left) >= height(node.left.right):
                    self.right_rotate(node)
                # node.left.right will move to node.right
                # if it contribute the height of node.left, then move to node.right will cause node.right too high
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) > 1 + height(node.left):
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)
            node = node.parent

    def delete(self, node: Node):
        Bst.delete(node)
        self.rebalance(node)
