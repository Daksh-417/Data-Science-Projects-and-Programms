a="abcdefghijklmnopqrstuvwxyz"
name=input("Enter name :-")
for i in range(len(name)):
    for j in range(len(a)):
        if name[i]==a[j]:
            print(name[i]," :- ",j+1)