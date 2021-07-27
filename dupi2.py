l = [1,1,2,5,3,11,1,2,3,3,3,2,5,6,6,65,56]
l.sort()
a = 0
for i in l:
    if l[a] in l[a+1:]:
        v=l[a]
        while v in l:
            l.remove(v)
    else:
        a+=1
print(l)
