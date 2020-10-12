from DataStrct.BST.contruct import BST

# stack = []
#     ptr = bst.root
#     while len(stack) > 0:
#         # temp=[t.val for t in stack]
#         # print(temp)
#         while ptr == None and len(stack) > 0:
#             ptr = stack.pop(-1)
#             print(ptr.val)
#             ptr=ptr.right
#         if ptr != None:
#             stack.append(ptr)
#             ptr = ptr.left
#先序
def traversal_first(bst):
    #stack=[bst.root]#error
    stack=[]
    ptr=bst.root
    while ptr!=None:
        print(ptr.val)
        stack.append(ptr)
        ptr=ptr.left
        while ptr == None and len(stack) > 0:
            ptr = stack.pop(-1).right




def traversal_middle(bst):
    stack = []
    ptr = bst.root
    while ptr != None:
        stack.append(ptr)
        ptr = ptr.left
        while ptr == None and len(stack) > 0:
            ptr = stack.pop(-1)
            print(ptr.val)
            ptr=ptr.right


def traversal_last(bst):
    stack = []
    ptr = bst.root
    while ptr != None:
        stack.append((ptr,2))
        ptr = ptr.left
        while ptr == None and len(stack) > 0:
            temp = stack.pop(-1)
            #ptr = temp[0].right#!!!
            if temp[1]-1==0:
                print(temp[0].val)
            else:
                stack.append((temp[0],1))
                ptr = temp[0].right

if __name__ == '__main__':
    bst=BST(4)
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    print("-----先序-----")
    traversal_first(bst)
    print("-----中序-----")
    traversal_middle(bst)
    print("-----后序-----")
    traversal_last(bst)