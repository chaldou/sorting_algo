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
    
v=[5,1,2,8,7,0,4,3]
print(v)
l=trirapide(v)
print(l)