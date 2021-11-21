import queue


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def levelwiseinput():
    q = queue.Queue()
    rootData = int(input("Enter the root Data"))

    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    q.put(root)

    while not q.empty():
        current_node = q.get()

        print("Enter left child of ", current_node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_node.left = leftChild
            q.put(leftChild)

        print("Enter the right Child of ", current_node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_node.right = rightChild
            q.put(rightChild)

    return root


def printTreeDetailed(root):
    if root == None:
        return
    print(root.data, end=" : ")
    if root.left != None:
        print("L", root.left.data, end=", ")
    if root.right != None:
        print("R", root.right.data, end=" ")
    print("")
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def printatK(root, k):
    if root == None:
        return
    if k == 0:
        print(root.data)
    printatK(root.left, k-1)
    printatK(root.right, k-1)


def printNodeK(root, node, k):
    if root == None:
        return -1
    if root.data == node:
        printatK(root, k)
        return 0
    lD = printNodeK(root.left, node, k)
    if lD != -1:
        if lD + 1 == k:
            print(root.data)
        else:
            printatK(root.right, k-lD-2)
        return 1 + lD

    rD = printNodeK(root.right, node, k)
    if rD != -1:
        if rD + 1 == k:
            print(root.data)
        else:
            printatK(root.left, k-rD-2)
        return 1+rD
    return -1


root = levelwiseinput()

printNodeK(root, 5, 2)
