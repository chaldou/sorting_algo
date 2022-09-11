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



v=[3,6,7,4,5,1,0]
print(v)
a=tri_selection(v)
print(a)