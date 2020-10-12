#建树的思想
#treenode，tree-root
#定义函数/操作
class TreeNode:
    # def __init__(self,x=None,l=None,r=None):
    #     self.val=x
    #     self.left=l
    #     self.right=r
    def __init__(self,x=None):
        self.val=x
        self.left=None
        self.right=None


class BST():
    def __init__(self,root=None):
        root=TreeNode(root)
        self.root=root

    def insert(self,x):
        parent,ptr=self.root,self.root
        while ptr!=None:
            parent=ptr
            if ptr.val<x:
                ptr=ptr.right
            elif ptr.val>x:
                ptr=ptr.left
            else:
                print("error:insert fail,value of "+str(x)+" is exist!")
                return
        if parent.val>x:
            parent.left=TreeNode(x)
        else:
            parent.right=TreeNode(x)

if __name__ == '__main__':
    pass
