#appending list in dictionary
d={'name':'alice',10:25,'age':[10,20,30]}
#appending keys in dictionary
d1=[]
for i in d:
    print(i)
    d1.append(i)
print(d1)
# appending for values
g=[]
for i in d:
    y=d.get(i)
    g.append(y)
print(g)
