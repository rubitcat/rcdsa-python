from rcdsa.datastruct import AVLTree

def test_avl_tree_insert_delete():
  avl = AVLTree()
  res_preorder = []
  res_inorder = []

  # RR
  #       10
  avl.insert(10)
  #       10
  #         \
  #         20
  avl.insert(20)
  #       20
  #      /  \
  #     10  30
  avl.insert(30)
  #       20
  #      /  \
  #     10  30
  #          \
  #          40
  avl.insert(40)
  #       20
  #      /  \
  #     10  40
  #        / \
  #       30 50 
  avl.insert(50)

  # RL
  #       30
  #      /  \           
  #     20  40
  #    /   / \            
  #   10  35 50 
  avl.insert(35)

  # LL
  #         30
  #      /     \           
  #     10     40
  #    /  \   /  \            
  #   5   20 35  50     
  avl.insert(5)

  # LR
  #         30
  #      /     \           
  #     10     40
  #    /  \   /  \            
  #   5   20 35  50   
  #      /
  #     15
  avl.insert(15)
  #         30
  #      /     \           
  #     10     40
  #    /  \   /  \            
  #   5   20 35  50   
  #  /   /
  # 1   15
  avl.insert(1)
  #         30
  #      /     \           
  #     10     40
  #    /  \   /  \            
  #   5   20 35  50   
  #  /   / \ 
  # 1   15 25
  avl.insert(25)
  #         20
  #      /      \          
  #     10      30 
  #    /  \    /  \
  #   5   15  25  40
  #  /    /      /  \
  # 1    12     35  50
  avl.insert(12)

  avl.traversal_preorder(lambda v: res_preorder.append(v))
  avl.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == [20, 10, 5, 1, 15, 12, 30, 25, 40, 35, 50]
  assert res_inorder == [1, 5, 10, 12, 15, 20, 25, 30, 35, 40, 50]

  
  #         20
  #      /      \          
  #     10      30 
  #    /  \    /  \
  #   5   15  25  40
  #  /           /  \
  # 1           35  50
  avl.delete(12)
  # LL
  #         20
  #      /      \          
  #     5       30 
  #    /  \    /  \
  #   1   10  25  40
  #              /  \
  #             35  50
  avl.delete(15)
  # RR
  #         25
  #      /      \          
  #     5       40 
  #    /  \    /  \
  #   1   10  30  50
  #            \
  #             35
  avl.delete(20)

  res_preorder.clear()
  res_inorder.clear()
  avl.traversal_preorder(lambda v: res_preorder.append(v))
  avl.traversal_inorder(lambda v: res_inorder.append(v))
  assert res_preorder == [25, 5, 1, 10, 40, 30, 35, 50]
  assert res_inorder == [1, 5, 10, 25, 30, 35, 40, 50]