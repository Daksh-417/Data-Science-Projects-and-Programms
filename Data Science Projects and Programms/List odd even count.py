a=[12,324,5321,12,4215,1234,122,33,4213]
even=[]
c=0
b=0
odd=[]
for i in range(0,9):
    if a[i]%2==0:
        even.append(a[i])
        print(f"even no.{a[i]}")
    else:
        odd.append(a[i])
for j in even:
    c+=j
print(f"sum of even no.{c}")
for e in odd:
    b+=e
print(f"sum of odd no.{b}")