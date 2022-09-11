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

l=[11,39,9,2,8,87,92,63,74,6,5,69,64,33,46]
print(l)
v=tri_fusion(l)
print(v)