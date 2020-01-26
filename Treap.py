import random
class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
        self.priority = None
        if self.priority is None:
            self.priority = random.randint(1,200)

class Treap:
    def __init__(self):
        self.root = None
    def Rotate_left(self,root):
       x = root.right
       y = root.right.left
       x.left = root
       root.right = y
        #root = x
       return x
       
    def Rotate_right(self,root):
        l = root.left
        r = root.left.right
        l.right = root
        root.left = r
        return l
        
    def __Insert(self,root,value):
        if root == None:
            root = Node(value)
            return root
        else:
            if value < root.value:
                root.left = self.__Insert(root.left,value)
                if root.left.priority > root.priority:
                    root = self.Rotate_right(root)
            else:
                root.right = self.__Insert(root.right,value)
                if root.right.priority > root.priority:
                    root = self.Rotate_left(root)
        return root
    def Insert(self,value):
        self.root = self.__Insert(self.root,value)
        
    def InOrder(self):
        return self.__InOrder(self.root)
    def __InOrder(self,root):
        if root:
            self.__InOrder(root.left)
            print(root.value,root.priority)
            self.__InOrder(root.right)
            
    def PreOrder(self):
        return self.__PreOrder(self.root)
    def __PreOrder(self,root):
        if root:
            print(root.value,root.priority)
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)
            
    def PostOrder(self):
        return self.__PostOrder(self.root)
    def __PostOrder(self,root):
        if root:
            self.__PostOrder(root.left)
            self.__PostOrder(root.right)
            print(root.value,root.priority)
            
    def Search(self,value):
        return self.__Search(self.root,value)
    def __Search(self,root,value):
        if root == None:
            return False
        if root.value == value:
            return True
        l = self.__Search(root.left,value)
        if l:
            return True
        r = self.__Search(root.right,value)
        return r
    
    def Delete(self,value):
        return self.__Delete(self.root,value)
    def __Delete(self,root,value):
        if root is not None:
            if root.value == value:
                if root.left is None and root.right is None:
                    return None
                else:
                    if root.left is None:
                        return root.right
                    elif root.right is None:
                        return root.left
                    else:
                        if root.right.priority > root.left.priority:
                            self.Rotate_left(root)
                            root.left = self.__Delete(root.left,value)
                        else:
                            self.Rotate_right(root)
                            root.right = self.__Delete(root.right,value)
            elif value < root.value:
                root.left = self.__Delete(root.left,value)
            elif value > root.value:
                root.right = self.__Delete(root.right,value)
        return root    
