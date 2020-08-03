"""Main module."""
from typing import AnyStr
import json


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

        last_idx, ans, Null = 0, [], [None]
        queue = [(root, 0)]
        while queue:
            for _ in range(len(queue)):
                node, idx = queue.pop(0)
                if node.left: queue.append((node.left, 2 * idx + 1))
                if node.right: queue.append((node.right, 2 * idx + 2))

                ans += Null * (idx - last_idx - 1)
                ans.append(node.val)
                last_idx = idx

        return json.dumps(ans)

    @classmethod
    def deserialize_treenode(cls, data: AnyStr) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = json.loads(data)
        if not vals: return

        cursor = 1
        root = TreeNode(vals[0])
        layer = [root]
        while layer:
            node = layer.pop(0)
            if vals[cursor] is not None:
                node.left = TreeNode(vals[cursor])
                layer.append(node.left)
            cursor += 1

            if vals[cursor] is not None:
                node.right = TreeNode(vals[cursor])
                layer.append(node.right)
            cursor += 1

        return root
