#dictionary
#allowed list,tuple,and string also
d={'name':'alice',10:25,'age':[10,20,30]}
print(d['age'][2])
print(d['name'])
print(d[10])
#updation
d['age']=[30,40,50]
print(d)
#accessing keys
print(d.keys())
#accessing values
print(d.values())
print(d.get('age'))
