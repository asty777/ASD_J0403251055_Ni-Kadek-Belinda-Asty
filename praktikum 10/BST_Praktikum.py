data = [35, 75, 25, 45, 65, 85, 40]
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    
    return root


def inorderTraversal(root, result):
    if root:
        inorderTraversal(root.left, result)
        result.append(root.data)
        inorderTraversal(root.right, result)


def preorderTraversal(root, result):
    if root:
        result.append(root.data)
        preorderTraversal(root.left, result)
        preorderTraversal(root.right, result)


def postorderTraversal(root, result):
    if root:
        postorderTraversal(root.left, result)
        postorderTraversal(root.right, result)
        result.append(root.data)


nama = "Ni Kadek Belinda Asty"
nim = "J0403251055"

root_value = 55
data = [35, 75, 25, 45, 65, 85, 40]

root = Node(root_value)

for d in data:
    insert(root, d)

inorder = []
preorder = []
postorder = []

inorderTraversal(root, inorder)
preorderTraversal(root, preorder)
postorderTraversal(root, postorder)

print("Nama :", nama)
print("NIM  :", nim)
print("In-order  :", inorder)
print("Pre-order :", preorder)
print("Post-order:", postorder)