from Treap import *
def test():
    treap = Treap()
    treap.Insert(5)
    treap.Insert(2)
    treap.Insert(1)
    treap.Insert(8)
    treap.Insert(6)
    treap.Insert(7)
    print("INORDER TRAVERSAL:")
    treap.InOrder()
    print("PREORDER TRAVERSAL:")
    treap.PreOrder()
    print("POSTORDER TRAVERSAL:")
    treap.PostOrder()
    treap.Delete(1)
    print("TREE AFTER DELETION:")
    treap.InOrder()
    print("SEARCHING:")
    treap.Search(9)
    treap.Search(7)

if __name__ == '__main__':
    test()
