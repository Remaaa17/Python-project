import os
os.system("cls")

# we use self to refer to some instance 
# we use oop to group different objects that have same type
# procedural attributes is the " method also named behivor"

## setter , getter is used to set variable , and get it  ... we use it because this ( good style , easy to maintain code )
## defult argument ( variable has defult value )

class person :
    name = ""
    age = 0
    num = 0
    def __init__(self , name , age = 0): # age is defult argument
        self.name = name
        self.age = age 
        person.num += 1 # this giva all object unique id 
        print (f"object id : {person.num}")

    def PrintDetails (self):
        print(f"your anme is {self.name} \nyour age is {self.age}")
    def SetName (self,name): # setter
        self.name =name
    def  GetName (self): # getter
        return self.name

## inhertance 
class employee (person):
    def __init__(self, name, age , id , salary):
        super().__init__(name, age) # that use parent fucution 
        self.id = id
        self.salary = salary
    def PrintDetails (self): # this is overloading
        print(f"your anme is {self.name} \nyour age is {self.age} \nyour id is {self.id} \nyour sallay is {self.salary}")

ahmed= employee ("ahmed" , 19 , 20220012 , 2000)
ahmed.SetName("ahmed shreif")
ahmed.PrintDetails()
print()
mohamed = person ("ahmed" , 5)
mohamed.PrintDetails()

# PYTHON NOT GREAT AT INFORMATION HIDING THAT LEAD TO USE PRIVATE , PROTECTED

## private variable
# __Vname as __ahmed ## mangling .... we can use it in parent class and we can use from setter , getter in parent only

## protected variable
# _VName as _ahmed ## we can edit and get value from getter and setter in class ( parent or child )

# penifit of inhertance 
## create your own collections of data
## organize information
## division of work
## access information in a consistent manner
## add layers of complexity
## decomposition and abstraction in programming