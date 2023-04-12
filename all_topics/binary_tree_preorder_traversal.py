# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # if root == None:
        #     return []
        # if (root.left == None) and (root.right == None):
        #     return [root.val]

        # res = [root.val]
        # if (root.left == None):
        #     res.extend(self.preorderTraversal(root.right))
        # elif (root.right == None):
        #     res.extend(self.preorderTraversal(root.left))
        # else:
        #     res.extend(self.preorderTraversal(root.left))
        #     res.extend(self.preorderTraversal(root.right))
        # return res

        return [] if not root else ([root.val] +
                                    self.preorderTraversal(root.left) +
                                    self.preorderTraversal(root.right))

        # iterative
        #                                     #  Ex: root = [1, 2,None, 3,4]
        # if not root: return []              #         __1
        # stack, ans = [root], []             #        /
        #                                     #       2
        # while stack:                        #      / \
        #     node = stack.pop()              #     3   4
        #     ans.append(node.val)            #
        #                                     #     node     node.left   node.right  stack    ans
        #     if node.right:                  #   –––––––––  –––––––––   –––––––––   ––––––  ––––––
        #         stack.append(node.right)    #                                       [1]     []
        #     if node. left:                  #       1          2         None       [2]     [1]
        #         stack.append(node.left )    #       2          3          4         [4,3]   [1,2]
        #                                     #       3        None        None       [4]     [1,2,3]
        #                                     #       4        None        None       [4]     [1,2,3,4]
        # return ans