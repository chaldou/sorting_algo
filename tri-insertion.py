def tri_insertion(l):
    n=len(l);
    for i in range(1,n):
        tmp=l[i]
        j=i-1
        while j>=0 and l[j]>tmp:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=tmp;
        
l=[11,39,9,2,8,87,92,63,74,6,5,69,64,33,46]
print(l)
tri_insertion(l)
print(l)