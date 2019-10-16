#实现二叉搜索树的基本功能（增删查）

class Node(object):
    "树的节点类"

    def __init__(self, data, lchild = None, rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinarySearchTree(object):
    "二叉搜索树"

    def __init__(self):
        self.root = root

    def add(self,data):
        "增加节点"

        newnode = Node(data)

        #如果树是空的
        if self.root == None:
            self.root = newnode
        else:
            cur =  self.root

            while True:
                if data > cur.data:
                    if cur.rchild == None:
                        cur.rchild = newnode
                        break
                    else:
                        cur = cur.rchild
                elif data < cur.data:
                    if cur.lchild == None:
                        cur.lchild = newnode
                        break
                    else:
                        cur = cur.lchild
                else:
                    pass                    #二叉搜索树不存在节点值相同的情况


    def search(self,data):
        "查询树中是否有查询的值,如果有则返回该节点"
        cur = self.root

        while cur != None:
            if data > cur.data:
                cur = cur.rchild
            elif data < cur.data:
                cur = cur.lchild
            else:
                return cur
        return None

    def findmin(self,node):
        "找到指定节点下的最小节点"
        cur = node
        while cur.lchild != None:
            cur = cur.lchild

        return cur 

    def findmax(self,node):
        "找到指定节点下的最大值"
        cur = node 
        while cur.rchild != None:
            cur = cur.rchild

        return cur

    def delete(self,data):
        "删除指定值的节点"
        cur = self.root
        if cur.data < data:
            cur.rchild = self.delete(cur.data)
        elif cur.data > data:
            cur.lchild = self.delete(cur.data)
        else:
            if cur.lchild != None and cur.rchild != None:
                temp = self.findmin(cur.rchild)
                cur.data = temp.data
                cur.rchild = self.delete(cur.rchild)
            else:
                if cur.lchild != None:
                    cur = cur.lchild
                else:
                    cur =  cur.rchild

        return cur

"""
删除操作较为复杂
    第一种情况：要删除的是叶子节点，直接删除，将父节点的左孩子或者右孩子设为None
    第二种情况：要删除的节点有一个左节点或者右节点，删除该节点后，将该节点的孩子节点放到删除节点位置
    第三种情况：要删除的节点左右节点都有，删除该节点后，需要将该节点右子树上的最小值，放到删除节点位置，然后还要删除那个最小的节点
"""

            
            
            
            

        




        
