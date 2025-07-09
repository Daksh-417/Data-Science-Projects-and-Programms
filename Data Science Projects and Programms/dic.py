number={"student1":59,"student2":45,"student3":82}
g=[]
for i in number:
    n=number.get(i)
    g.append(n)
    max(g)
print(g)
