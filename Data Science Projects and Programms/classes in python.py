class Person:
     def __init__(self,name,age):#constructor-it is called automatically when object is called
         self.name= name
         self.age= age
         
     def myfunc(self):
         print("hello my name is " +self.name)

         
p1 = Person("John",36)
print(p1.name)
print(p1.age)
p1.myfunc()
