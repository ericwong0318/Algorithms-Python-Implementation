class Node(object):
    def __init__(self, key, parent=None, terminates=False):
        self.key = key
        self.terminates = False
        self.parent = parent
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node('')

    def find(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node if node.terminates else None  # node is leaf

    def insert(self, word):
        node = self.root
        parent = None
        for char in word:
            # char exist
            if char in node.children[char]:
                node = node.children
            # char not exist
            else:
                node.children[char] = Node(char, parent=node)
                node = node.children[char]
        node.terminates = True

    def remove(self, word):  # ???
        node = self.find(word)
        if node is None:
            raise KeyError('word not exist')

        node.terminates = False
        parent = node.parent
        # go up until the root
        while parent is not None:
            if node.children or node.terminates:
                return
            del parent.children[node.key]
            node = parent
            parent = parent.parent

    def list_word(self): #???
        result = []
        curr_word = ''
        self._list_word(self.root, curr_word, result)
        return result

    def _list_word(self, node, curr_word, result):
        for key, child in node.children.items():
            if child.terminates:
                result.append(curr_word + key)
            self._list_word(child, curr_word + key, result)
