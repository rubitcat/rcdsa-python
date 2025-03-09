from rcdsa.datastruct import BinarySearchTree

def test_binary_search_tree_insert_delete():
  bst = BinarySearchTree()
  res_preorder = []
  res_inorder = []

  #      50
  #     /  \
  #    30   70
  #   / \   / \
  #  20 40 60 80
  bst.insert(50)
  bst.insert(30)
  bst.insert(20)
  bst.insert(40)
  bst.insert(70)
  bst.insert(60)
  bst.insert(80)
  bst.traversal_preorder(lambda v: res_preorder.append(v))
  bst.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == [50, 30, 20, 40, 70, 60, 80]
  assert res_inorder == [20, 30, 40, 50, 60 ,70, 80]

  #      50
  #     /  \
  #    30   70
  #     \   / \
  #     40 60 80
  res_preorder.clear()
  res_inorder.clear()
  bst.delete(20)
  bst.traversal_preorder(lambda v: res_preorder.append(v))
  bst.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == [50, 30, 40, 70, 60, 80]
  assert res_inorder == [30, 40, 50, 60 ,70, 80]

  #      50
  #     /  \
  #    40   70
  #         / \
  #        60 80
  res_preorder.clear()
  res_inorder.clear()
  bst.delete(30)
  bst.traversal_preorder(lambda v: res_preorder.append(v))
  bst.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == [50, 40, 70, 60, 80]
  assert res_inorder == [40, 50, 60 ,70, 80]

  #      50
  #     /  \
  #    40   80
  #         / 
  #        60 
  res_preorder.clear()
  res_inorder.clear()
  bst.delete(70)
  bst.traversal_preorder(lambda v: res_preorder.append(v))
  bst.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == [50, 40, 80, 60]
  assert res_inorder == [40, 50, 60 ,80]

  #      50
  #     /  \
  #    40   85
  #         / \     
  #        60  90
  #           /
  #          87
  res_preorder.clear()
  res_inorder.clear()
  bst.insert(90)
  bst.insert(85)
  bst.insert(87)
  bst.delete(80)
  bst.traversal_preorder(lambda v: res_preorder.append(v))
  bst.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == [50, 40, 85, 60, 90, 87]
  assert res_inorder == [40, 50, 60 ,85, 87, 90]

  assert bst.search(87) == 87
  assert bst.search(100) is None