class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

import queue
def takeinput():
    q=queue.Queue()
    print("ENTER THE VALUE OF ROOT : ")
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=BinaryTree(rootdata)
    q.put(root)
    while (not(q.empty())):
        curr=q.get()
        print("ENTER THE VALUE OF LEFTCHILD OF",curr.data,": ")
        leftdata=int(input())
        if leftdata!=-1:
            leftchild=BinaryTree(leftdata)
            curr.left=leftchild
            q.put(leftchild)
        print("ENTER THE VALUE OF RIGHTCHILD OF",curr.data,": ")
        rightdata=int(input())
        if rightdata!=-1:
            rightchild=BinaryTree(rightdata)
            curr.right=rightchild
            q.put(rightchild)        
    return root
            
def printTree(root):
    if root==None:
        return
    inputq=queue.Queue()
    outputq=queue.Queue()
    inputq.put(root)
    while (not(inputq.empty())):
        while (not(inputq.empty())):
            curr=inputq.get()
            print(curr.data,end=" ")
            if curr.left!=None:
                outputq.put(curr.left)
            if curr.right!=None:
                outputq.put(curr.right)
        print()
        inputq,outputq=outputq,inputq
        
def zigzagtree(root):
    if root==None:
        return
    s1=[]
    s2=[]
    s1.append(root)
    currlevelremaining=1
    nextlevelcount=0
    flag=True
    while len(s1)!=0 or len(s2)!=0:
        if flag:
            top=s1.pop()
            print(top.data,end=" ")
            currlevelremaining-=1
            if top.left!=None:
                s2.append(top.left)
                nextlevelcount+=1
            if top.right!=None:
                s2.append(top.right)
                nextlevelcount+=1
            if currlevelremaining==0:
                print()
                currlevelremaining=nextlevelcount
                nextlevelcount=0
                flag=False
        else:
            top=s2.pop()
            print(top.data,end=" ")
            currlevelremaining-=1
            if top.right!=None:
                s1.append(top.right)
                nextlevelcount+=1
            if top.left!=None:
                s1.append(top.left)
                nextlevelcount+=1
            if currlevelremaining==0:
                print()
                currlevelremaining=nextlevelcount
                nextlevelcount=0
                flag=True        

root=takeinput()
print("ORIGINAL BINARY TREE IS :")
printTree(root)
print("ZIGZAG OF THE BINARY TREE IS :")
zigzagtree(root)