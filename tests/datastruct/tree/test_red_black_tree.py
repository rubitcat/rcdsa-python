from rcdsa.datastruct import RedBlackTree

def test_red_black_tree_insert_delete():
  rbt = RedBlackTree()
  res_preorder = []
  res_inorder = []
  
  # RR
  #     30b
  rbt.insert(30)
  #     30b
  #       \
  #       40r
  rbt.insert(40)
  #     40b
  #    /   \
  #   30r   50r
  rbt.insert(50)

  # UNCLE RED
  #     40b
  #    /   \
  #   30b   50b
  #         /
  #        45r
  rbt.insert(45)

  # RL
  #       40b
  #    /      \
  #   30b      50b
  #     \      /
  #     35r   45r
  rbt.insert(35)
  #         40b
  #      /      \
  #     34b      50b
  #    /  \      /
  #   30r  35r  45r  
  rbt.insert(34)

  # LR
  #         40b
  #      /      \
  #     34b      48b
  #    /  \      /  \
  #   30r  35r  45r 50r
  rbt.insert(48)

  # LL
  #         40b
  #      /      \
  #     34r      48b
  #    /  \      /  \
  #   30b  35b  45r 50r
  #   /
  #  25r
  rbt.insert(25)
  #         40b
  #      /      \
  #     34r      48b
  #    /  \      /  \
  #   25b  35b  45r 50r
  #   /  \
  #  10r  30r
  rbt.insert(10)

  rbt.traversal_preorder(lambda v: res_preorder.append(v))
  rbt.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == [40, 34, 25, 10, 30, 35, 48, 45, 50]
  assert res_inorder == [10, 25, 30, 34, 35, 40, 45, 48, 50]

  # simple case
  #         40b
  #      /      \
  #     34r      48b
  #    /  \      /  \
  #   25b  35b  45r 50r
  #     \
  #     30r
  rbt.delete(10)

  
  #  double black with sibling black red , LR case
  #         40b
  #      /      \
  #     30b      48b
  #    /  \      /  \
  #   25r  34r  45r 50r
  rbt.delete(35)
  
  #  double black with sibling black black
  #         40b
  #      /      \
  #     30b      48b
  #       \      /  \
  #       34r  45r 50r
  rbt.delete(25)
  
  #  double black with sibling black black
  #         40b
  #      /      \
  #     30b      48b
  #       \      /  \
  #       34r  45r 50r
  rbt.delete(34)
  #         48b
  #      /      \
  #     40b      50b
  #       \      
  #       45r  
  rbt.delete(30)

  res_preorder.clear()
  res_inorder.clear()  
  rbt.traversal_preorder(lambda v: res_preorder.append(v))
  rbt.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == [48, 40, 45, 50]
  assert res_inorder == [40, 45, 48, 50]
  
def test_aaa():

  rbt = RedBlackTree()
  res_inorder = []
  res_levelorder = [] 

  rbt.insert(7)
  rbt.insert(3)
  rbt.insert(18)
  rbt.insert(10)
  rbt.insert(22)
  rbt.insert(8)
  rbt.insert(11)
  rbt.insert(26)
  rbt.insert(2)
  rbt.insert(6)
  rbt.insert(13)

  rbt.traversal_inorder(lambda v: res_inorder.append(v))
  rbt.traversal_levelorder(lambda v: res_levelorder.append(v))
  assert res_inorder == [2,3,6,7,8,10,11,13,18,22,26]
  assert res_levelorder == [10,7,18,3,8,11,22,2,6,13,26]


  rbt.delete(18)
  rbt.delete(11)
  rbt.delete(3)
  rbt.delete(10)
  rbt.delete(22)

  res_inorder.clear()
  res_levelorder.clear()
  rbt.traversal_inorder(lambda v: res_inorder.append(v))
  rbt.traversal_levelorder(lambda v: res_levelorder.append(v))
  assert res_inorder == [2, 6, 7, 8, 13, 26 ]
  assert res_levelorder == [13, 7, 26, 6, 8, 2 ]


