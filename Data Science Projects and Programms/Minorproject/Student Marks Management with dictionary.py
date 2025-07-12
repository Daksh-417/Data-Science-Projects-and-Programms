# #Student Marks Management

# 👉 Create a Python program to:
# 	•	Store student names as keys and marks as values in a dictionary.
# 	•	Allow adding new students with marks.
# 	•	Allow updating marks of existing students.
# 	•	Display highest, lowest, and average marks.
# 	•	Show all records.
sum=0
number={'student1':23,'student2':33,'student3':43,'student4':53}
number['student5']=63# insertion
number['student1']=90 #updation
g=number.values()
print(f'marks of 5 students={list(g)}')
print(f'highest number={max(g)}')
print(f'lowest number={min(g)}')
for i in g:
    sum+=i
    avg= sum//5
print(f'Average number={avg}')
print(number)
