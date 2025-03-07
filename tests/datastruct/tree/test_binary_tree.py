from rcdsa.datastruct import BinaryTree


preorder_list = [0, 1, 3, 4, 2, 5, 6]
inorder_list = [3, 1, 4, 0, 5, 2, 6]
postorder_list = [3, 4, 1, 5, 6, 2, 0]
levelorder_list = [0, 1, 2, 3, 4, 5, 6]
pindex_list = [-1, 0, 0, 1, 1, 2, 2]

def test_binary_tree_insert_and_delete():

  bt = BinaryTree()
  res_preorder = []
  res_inorder = []

  # insert
  for i in range(len(levelorder_list)):
    bt.insert(levelorder_list[i])
  bt.traversal_preorder(lambda v: res_preorder.append(v))
  bt.traversal_inorder(lambda v: res_inorder.append(v))
  assert [0, 1, 3, 4, 2, 5, 6] == res_preorder
  assert [3, 1, 4, 0, 5, 2, 6] == res_inorder

  # delete
  res_preorder.clear()
  res_inorder.clear()
  bt.delete(1)
  bt.delete(0)
  bt.traversal_preorder(lambda v : res_preorder.append(v))
  bt.traversal_inorder(lambda v: res_inorder.append(v))
  assert [5, 6, 3, 4, 2] == res_preorder
  assert [3, 6, 4, 5, 2] == res_inorder

def test_binary_tree_traversal():
  
  bt = BinaryTree()
  for i in range(len(levelorder_list)):
    bt.insert(levelorder_list[i])
  res_trav = []

  # pre order traversal
  res_trav.clear()
  bt.traversal_preorder(lambda v: res_trav.append(v))
  assert res_trav == preorder_list

  # in order traversal
  res_trav.clear()
  bt.traversal_inorder(lambda v: res_trav.append(v))
  assert res_trav == inorder_list

  # post order traversal
  res_trav.clear()
  bt.traversal_postorder(lambda v: res_trav.append(v))
  assert res_trav == postorder_list

  # level order traversal
  res_trav.clear()
  bt.traversal_levelorder(lambda v: res_trav.append(v))
  assert res_trav == levelorder_list

def test_binary_tree_serialize():
  
  bt = BinaryTree()
  bt.load_from_parent_levelorder_seq(pindex_list, levelorder_list, len(pindex_list))
  res_preorder = []
  res_inorder = []
  res_levelorder = []
  bt.traversal_preorder(lambda v: res_preorder.append(v))
  bt.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == preorder_list
  assert res_inorder == inorder_list

  pindex_seq_back, levelorder_seq_back, count = bt.get_parent_levelorder_seq()
  assert pindex_seq_back == pindex_list
  assert levelorder_seq_back == levelorder_list
  assert count == len(pindex_list)


def test_completed_binary_tree_serialize():
  
  bt = BinaryTree()
  bt.load_from_cbt_levelorder_seq(levelorder_list, len(levelorder_list))
  res_preorder = []
  res_inorder = []
  res_levelorder = []
  bt.traversal_preorder(lambda v: res_preorder.append(v))
  bt.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == preorder_list
  assert res_inorder == inorder_list

  res_levelorder = bt.get_levelorder_seq()
  assert res_levelorder == levelorder_list
  