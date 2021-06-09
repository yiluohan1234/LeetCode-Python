#定义二叉树结点类型
class TreeNode:
    """docstring for BiTNode"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#前序遍历
def pre_order(root):
    #先判断二叉树是否为空
    #if root.left_child is None and root.right_child is None:
    if root is None:
        return root
    #先根
    print(root.val)
    #再左
    if root.left is not None:
        pre_order(root.left)
    #再右
    if root.right is not None:
        pre_order(root.right)

#中序遍历二叉树
def mid_order(root):

    #先判断二叉树是否为空,当左右节点都为空时
    if root is None:
        return
    #中序遍历 左根右
    #遍历左子树
    if root.left is not None:
        mid_order(root.left)
    #遍历根节点
    print(root.val)
    #遍历右子树
    if root.right is not None:
        mid_order(root.right)

#后序遍历
def after_order(root):
    #先判断二叉树是否为空
    if root is None:
        return root
    #再左
    if root.left is not None:
        after_order(root.left)
    #再右
    if root.right is not None:
        after_order(root.right)
    #先根
    print(root.val)

def list_to_bitree(array):
    #判断arr是否为空
    if len(array) == 0:
        return TreeNode(array[0])
    mid=len(array) // 2 # 有序数组的中间元素的下标
    #print(mid)
    #start=0 # 数组第一个元素的下标
    #end=-1 # 数组最后一个元素的下标
    if len(array) > 0:
        #将中间元素作为二叉树的根
        root = TreeNode(array[mid])
        #如果左边的元素个数不为零，则递归调用函数，生成左子树
        if len(array[:mid]) > 0:
            root.left = list_to_bitree(array[:mid])
    #如果右边的元素个数不为零，则递归调用函数，生成左子树
    if len(array[mid+1:]) > 0:
        root.right = list_to_bitree(array[mid+1:])
    return root


'''  
     3
    / \
   4   5
  / \   \ 
 1   3   1
 '''
#将[0,1,2,3,4,5,6,7,8,9,10]存储到二叉树
if __name__ == '__main__':
    #先构造一个有序数组、链表
    arr=[3,4,5,1,3,None,1]
    #调用函数
    BT=list_to_bitree(arr)
    #前序遍历二叉树
    print("前序")
    pre_order(BT)
    # 中序遍历二叉树
    print("中序")
    mid_order(BT)
    # 后序遍历二叉树
    print("后序")
    after_order(BT)