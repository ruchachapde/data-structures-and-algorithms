#Class defination for Binary Search Tree
class BinarySearchTreeNode:
  def __init__(self, data):
    self.val = data
    self.left = None
    self.right = None

def insertDataBST(root, data):
  if root is None:
    return BinarySearchTreeNode(data)
  
  elif root.val == data:
    return root

  elif root.val < data:
    root.right = insertDataBST(root.right, data)

  elif root.val > data:
    root.left = insertDataBST(root.left, data)

  return root

#Inorder Traversal
def inorderTraversal(root):
  if root is None:
    return

  inorderTraversal(root.left)
  print(root.val, end=" ")
  inorderTraversal(root.right)





# function defination for searching the element in BST
# Best and average case colpmexity is O(log n)
# Worst case complexity in case of skewed binary search tree is O(n)
def searchDataBST(root, target):
  if root is None:
    return False
  
  elif root.val < target:
    return searchDataBST(root.right, target)

  elif root.val > target:
    return searchDataBST(root.left, target)

  return True



#function defination to find minimum value from right subtree
def minValue(node):
  current = node
  while current:
    current = current.left
  return current


# function defination for deleting a node
def deleteNode(root, key):
  if root is None:
    return root

  #Search for the key either in left or right
  elif root.val < key:
    root.right = deleteNode(root.right, key)

  elif root.val > key:
    root.left = deleteNode(root.left, key)

  else:
    #easy case where you have one child node only
    if root.left is None:
      return root.right

    elif root.right is None:
      return root.left

    # difficult case where both child nodes and then subtree
    tempNode = minValue(root.right)
    root.data = tempNode
    root.right = deleteNode(root.right, tempNode.val)
  return root


#Driver Code
root = BinarySearchTreeNode(100)
root = insertDataBST(root, 80)
root = insertDataBST(root, 120)
root = insertDataBST(root, 70)
root = insertDataBST(root, 85)
root = insertDataBST(root, 110)
root = insertDataBST(root, 130)


#Function calling to print the data in tree
inorderTraversal(root)

#Function calling for Search Data in BST
searchDataBST(root, 120)

#function calling for deleting a node
deletedKey = deleteNode(root,110)

print("After deletion of node inorder traversal will be")

inorderTraversal(root)