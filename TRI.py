#1) //////////// PAR SELECTION ////////////////////
def tri_selection(l):
    for i in range(len(l)):
        min = i
        for j in range(i+1, len(l)):
            if l[min] > l[j]:
                min = j
        tmp = l[i]
        l[i] = l[min]
        l[min] = tmp
    return l



#v=[3,6,7,4,5,1,0]
#print(v)
#a=tri_selection(v)
#print(a)


#2) ////////////////////// PAR TAS /////////////////////
def sort_heapsort(l):
    n = len(l)
    # Il n'y a que n // 2 racine dans le tas, le reste sont des feuilles
    for i in range(n // 2 - 1, -1, -1):
        restore_heap_properties(l, n, i)

    for i in range(n-1, 0, -1):
        l[i], l[0] = l[0], l[i]
        restore_heap_properties(l, i, 0)
    return l

# restore_heap_properties(liste, dernier indice, racine à évaluer)
def restore_heap_properties(l, n, i):
    maxVal = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and l[maxVal] < l[left]:
        maxVal = left

    if right < n and l[maxVal] < l[right]:
        maxVal = right

    if maxVal != i:
        l[i], l[maxVal] = l[maxVal], l[i]
        restore_heap_properties(l, n, maxVal)


#l = [11, 39, 9, 2, 8, 87, 92, 63, 74, 6, 5, 69, 63, 33, 46]
#print(l)
#sort_heapsort(l)
#print(l)

#3) ///////////////// PAR BULLE ////////////////////////
    
def tribul(l):
    for n in range(len(l)-1, 0, -1):
        for i in range(n):
            if l[i]>l[i+1]:
                l[i], l[i+1]= l[i+1], l[i]
    return l
#v=[0,9,3,4,8,6,7,3,2,4]                
#tribul(v)   
#print(v)

#4) ///////////////////////////// TRI FUSION ////////////////////////////
def tri_fusion(l):
  if len(l)<=1:
    return l
  milieu = len(l)//2
  tab1 = l[:milieu]
  tab2 = l[milieu:]
  gauche = tri_fusion(tab1)
  droite = tri_fusion(tab2)
  fusionne = fusion(gauche,droite)
  return fusionne

def fusion(tab1,tab2):
  indice_tab1 = 0
  indice_tab2 = 0
  taille_tab1 = len(tab1)
  taille_tab2 = len(tab2)
  tab_fusion=[]
  while indice_tab1<taille_tab1 and indice_tab2 < taille_tab2:
    if tab1[indice_tab1] < tab2[indice_tab2]:
      tab_fusion.append(tab1[indice_tab1])
      indice_tab1+=1
    else:
      tab_fusion.append(tab2[indice_tab2])
      indice_tab2 +=1
  while indice_tab1 < taille_tab1:
    tab_fusion.append(tab1[indice_tab1])
    indice_tab1 +=1
  while indice_tab2<taille_tab2:
    tab_fusion.append(tab2[indice_tab2])
    indice_tab2 +=1
  return tab_fusion

#l=[11,39,9,2,8,87,92,63,74,6,5,69,64,33,46]
#print(l)
#v=tri_fusion(l)
#print(v)

#5) /////////////////// TRI RAPIDE /////////////////////////
def trirapide(L):
    def trirap(L,g,d):
        pivot = L[(g+d)//2]
        i=g
        j=d
        while True:
            while L[i]<pivot:
                i+=1
            while L[j]>pivot:
                j-=1
            if i>j:
                break
            if i<j:
                L[i], L[j] = L[j], L[i]
            i+=1
            j-=1
        if g<j:
            trirap(L,g,j)
        if i<d:
            trirap(L,i,d)
    g=0
    d=len(L)-1
    R=list(L)
    trirap(R,g,d)
    return R
    
#v=[5,1,2,8,7,0,4,3]
#print(v)
#l=trirapide(v)
#print(l)

#6) ////////////////// TRI PAR INSERTION //////////////////
def tri_insertion(l):
    n=len(l);
    for i in range(1,n):
        tmp=l[i]
        j=i-1
        while j>=0 and l[j]>tmp:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=tmp;
    return l
        
#l=[11,39,9,2,8,87,92,63,74,6,5,69,64,33,46]
#print(l)
#tri_insertion(l)
#print(l)

#7) ///////////// TRI ARBRE /////////////////////////////////

class SortTree:
  def __init__(self, value):
    self.left = None
    self.value = value
    self.right = None
  def insert_val(self, _value):
    if _value < self.value:
       if self.left is None:
         self.left = SortTree(_value)
       else:
         self.left.insert_val(_value)
    else:
       if self.right is None:
         self.right = SortTree(_value)
       else:
         self.right.insert_val(_value)

def display(_node):
   return list(filter(None, [i for b in [display(_node.left) if isinstance(_node.left, SortTree) else [getattr(_node.left, 'value', None)], [_node.value], display(_node.right) if isinstance(_node.right, SortTree) else [getattr(_node.right, 'value', None)]] for i in b]))



