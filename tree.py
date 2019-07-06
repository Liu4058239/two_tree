# 前序序列的第一个元素即为根节点，根据根节点的值在中序序列找到根节点的位置假定为i
# 则根据二叉树前序和中序的规律：
# 前序序列索引1~i构成子数列为根节点左子树的前序序列，i+1~n1构成子数列为根节点右子树的前序序列（n1为前序序列的长度）；
# 中序序列索引0~i-1构成子数列为根节点左子树的中序序列，i+1~n1构成子数列为根节点右子树的中序序列（n1为前序序列的长度）；
# 根节点的左节点为左子树的根节点，根节点的右节点为右子树的根节点
# 根据这样的规律一直递归下去，直到序列为空。



# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        val = tin.index(pre[0])
        root.left=self.reConstructBinaryTree(pre[1:val+1],tin[:val])
        root.right=self.reConstructBinaryTree(pre[val+1:],tin[val+1:])
        return root