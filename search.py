#i=1
'''while i < 11:
    print(i)
    i=i+1
    if i == 5:
       continue  
    print("Loop Continuing")
else
    print("while loop ended")    
    '''
#class MyClass:
#x = 5
#print(MyClass)

#p1 = MyClass()
#print(p1.x)
class person:
  def __init__(self,name,age):
   self.name = name
   self.age = age
   
  def myfunc(self):
    print("Hello my name is " + self.name)
    
p1 = person("john", "36")
p2 = person("Ryzen", "56")
p3 = person("Hobit", "26")
p4 = person("zed", "43")

#print(p1.name)
p1.myfunc()