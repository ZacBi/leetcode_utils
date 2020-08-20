"""Main module."""
from collections import deque, defaultdict
import json
from typing import AnyStr, Dict


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Trie:
    def __init__(self):
        # For empty string `""`
        self.trie = {'flag': True}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.trie
        for char in word:
            if char in node:
                node = node[char]
            else:
                node[char] = {}
                node = node[char]
        # indentify whether path is a word
        node['flag'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.trie
        for char in word:
            if char in node: node = node[char]
            else: return False
        return node.get('flag', False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.trie
        for char in prefix:
            if char in node: node = node[char]
            else: return False
        return True


class Codec:
    @classmethod
    def serialize_listnode(cls, head: ListNode) -> AnyStr:
        assert isinstance(head, ListNode)

        res = []
        while head:
            res.append(head.val)
            head = head.next

        return json.dumps(res)

    @classmethod
    def deserialize_listnode(cls, data: AnyStr) -> ListNode:
        vals = json.loads(data)

        assert isinstance(vals, list)
        if not vals: return

        head = ListNode(vals[0])
        cursor = head

        for val in vals[1:]:
            cursor.next = ListNode(val)
            cursor = cursor.next

        return head

    @classmethod
    def serialize_treenode(cls, root: TreeNode) -> AnyStr:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        assert isinstance(root, TreeNode)

        if not root: return "[]"

        ans, queue = [], deque(root)
        while queue:
            node = queue.popleft()
            if node:
                ans.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans.append(None)

        return json.dumps(ans)

    @classmethod
    def deserialize_treenode(cls, data: AnyStr) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        assert isinstance(data, str)

        vals = json.loads(data)
        if not vals: return

        cursor = 1
        root = TreeNode(vals[0])
        queue = deque(root)
        while queue or cursor < len(vals):
            node = queue.popleft()

            if vals[cursor] is not None:
                node.left = TreeNode(vals[cursor])
                queue.append(node.left)
            cursor += 1

            if vals[cursor] is not None:
                node.right = TreeNode(vals[cursor])
                queue.append(node.right)
            cursor += 1

        return root
