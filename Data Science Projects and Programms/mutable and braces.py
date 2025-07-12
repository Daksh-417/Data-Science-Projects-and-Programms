#set and list is mutable
#currly braces{}
s2={1,1,2,3,4}#multiple elements not included
print(s2)
for i in s2:
    if 1==i:
        print(i)
        break
    else:
        print("notfound")
        
