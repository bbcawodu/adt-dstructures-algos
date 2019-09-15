def BinaryTree(root):
    return [root, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


root = BinaryTree(3)
insertLeft(root, 4)
insertLeft(root, 5)
insertRight(root, 6)
insertRight(root, 7)
leftChild = getLeftChild(root)
print(leftChild)

setRootVal(leftChild, 9)
print(root)
insertLeft(leftChild, 11)
print(root)
print(getRightChild(getRightChild(root)))
