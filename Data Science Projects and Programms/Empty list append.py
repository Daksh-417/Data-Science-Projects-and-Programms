a = [23, [[]]]
name = input("Name :- ")
for i in a:
    if isinstance(i, list):
        for j in i:
            if j == []:
                j.append(name)
print(a)