#二叉树的实现

class Node(object):
    "树的节点类"

    def __init__(self, data = -1, lchild = None, rchild = None):
        "节点初始化，每个节点有3个属性"
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    "基本二叉树"

    def __init__(self):
        "初始化根节点"
        self.root = None

    def add(self,data):
        "增加节点(使用了队列)"

        newnode = Node(data)

        #如果树是空的
        if self.root == None:
            self.root = newnode
        else:
            queue = list()
            queue.append(self.root)

            while queue:
                cur = queue.pop()
                #左子树为空
                if cur.lchild == None:
                    cur.lchild = newnode
                    return
                #右子树为空
                elif cur.rchild == None:
                    cur.rchild = newnode
                    return
                #左右子树都不为空
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)            #这块卡了我好久，总算是弄明白了(使用的是队列不是栈)

    def preorder(self):
        "前序遍历（非递归方式实现，使用了栈）"
        cur = self.root
        stack = []

        #只要节点有值，并且栈不为空，说明还有节点没有遍历
        while cur != None or len(stack) != 0:
            #遍历左子树节点
            while cur != None:
                print(cur.data)
                stack.append(cur)
                cur = cur.lchild
            #跳转到右子树节点遍历
            if len(stack) != 0:
                cur = cur.pop(len(stack) - 1)
                cur = cur.rchild

    def preorderrecursion(self):
        "前序遍历（递归方式实现）"
        cur = self.root
        if cur != None:
            print(cur.data)
            self.preorderrecursion(cur.lchild)
            self.preorderrecursion(cur.rchild)

    def midorder(self):
        "中序遍历（非递归方式）"
        cur = self.root
        stack = []

        while cur != None or len(stack):
            while cur != None:
                stack.append(cur)
                cur = cur.lchild

            if len(stack):
                cur = cur.pop(len(stack) - 1)
                print(cur.data)
                cur = cur.rchild

    def migorderrecusion(self):
        "中序遍历（递归的方式）"
        cur = self.root
        if cur != None:
            self.migorderrecusion(cur.lchild)
            print(cur.data)
            self.migorderrecusion(cur.rchild)

    def postorder(self):
        "后序遍历（非递归）"
        cur = self.root
        lastvisit = root
        stack = []

        while cur != None or len(stack):
            while cur != None:
                stack.append(cur)
                cur = cur.lchild
            
            cur = stack[len(stack) - 1]
            #需要判断当前节点是否具有右节点，没有才能打印
            if cur.rchild == None or cur.rchild == lastvisit:
                print(cur.data)
                stack.pop(len(stack) - 1)
                lastvisit = cur
                cur = None
            else:
                cur = cur.rchild


    def postorderrecursion(self):
        "后序遍历（递归）"
        cur = self.root
        self.postorderrecursion(cur.lchild)
        self.postorderrecursion(cur.rchild)
        print(cur.data)




