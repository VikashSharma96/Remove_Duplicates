l = [1,1,1,2,2,4,453,34,34,4,1,1,1,3,2,452,22,1,45,55,0]
l.sort()
for i in l:
    c = l.pop(0)
    if c in l:
        while c in l:
            l.remove(c)
    else:
        l.append(c)
print(l)
