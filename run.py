from bst import BST


bst = BST()
bst.insert(10)
bst.insert(8)
bst.insert(15)
bst.insert(3)
bst.insert(9)
bst.insert(12)
bst.insert(20)


print("=========BFS===========")

bst.bfs()

print("")
print("=========DFS===========")

bst.dfs()
#
# bst.find(5)
# bst.find(10)
# bst.find(3)
# bst.find(30)

