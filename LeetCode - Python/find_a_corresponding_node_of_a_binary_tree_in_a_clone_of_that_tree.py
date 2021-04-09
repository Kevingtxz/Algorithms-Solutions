class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        nodes = []
        while True:
            if original == target:
                return cloned
            if original.left != None and original.right != None:
                nodes.append([original.right, cloned.right])
                original, cloned = original.left, cloned.left
            elif original.left != None:
                original, cloned = original.left, cloned.left
            elif original.right != None:
                original, cloned = original.right, cloned.right
            else:
                original, cloned = nodes[-1][0], nodes[-1][1]
                nodes.pop()
