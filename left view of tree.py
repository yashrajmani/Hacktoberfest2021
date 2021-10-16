class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
def left(root):
    if root == None:
        return 0
    q=[root]
    while (len(q)):
        n = len(q)
        for i in range(1, n + 1):
            temp = q[0]
            q.pop(0)
            if (i == 1):
                print(temp.data, end=" ")
            if (temp.left != None):
                q.append(temp.left)
            if (temp.right != None):
                q.append(temp.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
#print("call")
left(root)