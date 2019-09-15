class BinaryTree:
    def __init__(self,rootKey):
        self.rootKey = rootKey
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootKey(self, rootKey):
        self.rootKey = rootKey

    def getRootKey(self):
        return self.rootKey


r = BinaryTree('a')
print(r.getRootKey())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootKey())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootKey())
r.getRightChild().setRootKey('hello')
print(r.getRightChild().getRootKey())