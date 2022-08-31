"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # if (not root):
        #     return []
        
        # res = [root.val]
        # res.append(("#"))
        # while (root.left and root.right):
        #     root.next = root.left
        #     res.append(root.left)
        #     res.append(root.right)

        # BFS - Right to Left
        # need to populate next pointers of each node with nodes that occur to its immediate right on the same level
        # easily be done with BFS. Since for each node, we require the right node on the same level,
        # we will perform a right-to-left BFS instead of the standard left-to-right BFS
        # Before starting the traversal of each level, we would initialize a rightNode variable set to NULL
        # starting at rightmost node of each level. We set the next node of cur as rightNode and update rightNode = cur
        # ensure that each node would be assigned its rightNode properly while traversing from right to left
        # if cur has a child, we would first push its right child and only then its left child (since we are doing right-to-left BFS)
        # Once BFS is completed (after queue becomes empty), all next node would be populated and we can finally return root
        # Time Complexity : O(N), where N is the number of nodes in the given tree. We only traverse the tree once using BFS which requires O(N).
        # Space Complexity : O(W) = O(N), where W is the width of given tree. 
        # This is required to store the nodes in queue. Since the given tree is a perfect binary tree, its width is given as W = (N+1)/2 ≈ O(N)
        if not root: return None
        q = deque([root])
        while q:
            rightNode = None
            for _ in range(len(q)):
                cur = q.popleft()
                cur.next, rightNode = rightNode, cur
                if cur.right:
                    # push right, then left
                    q.extend([cur.right, cur.left])
        return root

        # DFS
        # populate the next pointers recursively using DFS
        # must update next pointers of the child of each node from the its parent's level itself
        # at each recursive call:
            # If child node exists
                # assign next of left child node as right child node: root -> left -> next = root -> right
                # assign next of right child node as left child of root's next (if root's next exists): root -> right -> next = root -> next -> left
                # If next node of current root is present 
                # (the next pointer of root would already be populated in above level) , 
                # the right immediate node of root's right child must be root's next's left child because if child of root exists, 
                # then the child of root's next must also exist.
            # If child node doesn't exist, we have reached the last level, we can directly return since there's no child nodes to populate their next pointers

        # Time Complexity : O(N), each node is only traversed once
        # Space Complexity : O(logN), required for recursive stack. 
        # The maximum depth of recursion is equal to the height of tree which in this case of perfect binary tree is equal to O(logN)
        if not root: return None
        L, R, N = root.left, root.right, root.next
        if L:
            L.next = R
            if N: R.next = N.left
            self.connect(L)
            self.connect(R)
        return root

        # BFS - Space-Optimized Appraoch
        # traverse in BFS manner but populate the next pointers of bottom level just as we did in the DFS solution
        # We first populate the next pointers of child nodes of current level. This makes it possible to traverse the next level without using a queue.
        # traverse to root's left child and repeat the process - traverse current level, fill next pointers of child nodes and then again update root = root -> left. 
        # So, we are basically performing standard BFS traversal in O(1) space by using next pointers to our advantage
        # continues till we reach the last level of tree
        # Time Complexity : O(N), we only traverse each node once, basically doing a standard BFS.
        # Space Complexity : O(1), only constant extra space is being used
        head = root
        while root:
            cur, root = root, root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next: cur.right.next = cur.next.left
                else: break
                cur = cur.next
                
        return head