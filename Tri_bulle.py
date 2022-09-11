def tri_bulle(l):
    n=len(l)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if l[j]>l[j+1]:
                l[j], l[j+1]= l[j+1], l[j]
l=[0,9,3,4,8,6,7,3,2,4]                
tri_bulle(l)               
for i in range(len(l)):
    print("%d" %l[i])
    
def tribul(l):
    for n in range(len(l)-1, 0, -1):
        for i in range(n):
            if l[i]>l[i+1]:
                l[i], l[i+1]= l[i+1], l[i]
v=[0,9,3,4,8,6,7,3,2,4]                
tribul(v)   
print(v)