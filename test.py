from TRI import *
l=[3,6,8,5,4]
v=tri_fusion(l)
print(v)
v=tri_selection(l)
print(v)
v=tribul(l)
print(v)
v=tri_insertion(l)
print(v)
v=trirapide(l)
print(v)
v=sort_heapsort(l)
print(v)
tree = SortTree(4)
for i in [5, 3, 1, 2, 8, 7, 4]:
  tree.insert_val(i)
print(display(tree))
