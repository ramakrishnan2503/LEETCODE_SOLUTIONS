# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst=[]
        ans=[]
        def traverse(root):
            if not root:
                return 
            traverse(root.left)
            lst.append(root.val)
            traverse(root.right)
        traverse(root)
        element_count = {}
        val=0
        for item in lst:
            element_count[item] = element_count.get(item, 0) + 1
            if element_count.get(item)>val:
                val=element_count.get(item) 
        
        for i in element_count.items():
            if i[1] == val:
                ans.append(i[0])
        return ans
            
        