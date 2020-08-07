"""Main module."""
from collections import deque
import json
from typing import AnyStr


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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
    def deserialize_treenode(cls, data: AnyStr) - > TreeNode:
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
