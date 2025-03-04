from rcdsa.datastruct import BinaryTree

# def test_binary_tree_create 

def test_completed_binary_tree_traversal():
  arr = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6]
  # bt = BinaryTree(arr)
  bt = BinaryTree(arr)

  # pre order traversal test
  preorder = []
  bt.traversal_preorder(bt.root, lambda v: preorder.append(v))
  assert [1, 2, 4, 6, 6, 5, 6, 3, 6, 6] == preorder

  # in order traversal test
  inorder = []
  bt.traversal_inorder(bt.root, lambda v: inorder.append(v))
  assert [6, 4, 6, 2, 6, 5, 1, 6, 3, 6] == inorder

  # post order traversal test
  postorder = []
  bt.traversal_postorder(bt.root, lambda v: postorder.append(v))
  assert [6, 6, 4, 6, 5, 2, 6, 6, 3, 1] == postorder

  # level order traversal test
  levelorder = []
  bt.traversal_levelorder(bt.root, lambda v: levelorder.append(v))
  assert [1, 2, 3, 4, 5, 6, 6, 6, 6, 6] == levelorder