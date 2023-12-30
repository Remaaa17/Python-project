import os
os.system("cls")

def ahmed ():
    """ahmed shreif ahmed amer """  #this command docummentaion funcition and we use it by help ##help(ahmed)

class person ():
    def __init__ (self,name,age): # constractor 
        self.name=name
        self.age=age
    def __add__ (self , other):
        return person("Name" , self.age + other)
    def __str__(self): # replace defult value when print ObjName
        return (f"my name is {self.name} , My age is : {self.age}")
ahmed = person ("ahmed" , 19)

a1 = ahmed + 20 
print (a1.age)

print(ahmed.name)

# # __del__ this is destarctor and it begin when call del ObjName ##del ahmed
# # __str__ when print ObjName we chage dfult value ( adress in ram , ClassName ) ## print(ahmed) ### defult is ==> <__main__.person object at 0x000001B49DC8AD10>
# # __add__ when use Obj in sum opperation we control on it when add it

# print(ahmed)
# del ahmed # remove Object From Ram


# to call method from parent class in child class 
## ParentClass.MethodName (self,pramter) in overlodded method

class person ():
    def __init__ (self,name,id): 
        self.name=name
        self.id=id
    def display (self):
        print(f"my name is {self.name} \nmy id is {self.id}")

class employee (person):
    def __init__ (self,name,id,age,sallery):
        self.age=age
        self.sallery=sallery
        person.__init__(self,name,id) # we use parent mehtod in overlodded method
ahmed = employee ("ahmed" , 20220012 , 19 , 2000)
ahmed.display()