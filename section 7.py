class parent1 :
    name = ""
    def __init__(self,name):
        self.name=name

class parent2 :
    def __init__ (self, mm) :
        self.mm = mm

## Multi level inheritance 
class Child1 (parent1):
    def __init__(self,name,age):
        self.age=age
        parent1.__init__(self,name)

class Child2 (Child1):
    def __init__(self,name,age,sallay):
        self.sallay=sallay
        Child1.__init__(self,name,age)

## multiple inheritance
class Child3 (parent1 , parent2):
    def __init__(self,name,age,id, mm):
        self.id=id
        parent1.__init__(self,name,age)
        parent2.__init__(self,mm)
    def PrintDetails (self):
        print(f" my id is {self.id}")

## overriding
class person :
    name = ""
    age = 0
    def __init__(self,name,age):
        self.name=name
        self.age = age
    def PrintDetails (self):
        print(f"my name is {self.name} \nmy age is {self.age}")

class employee (person):
    def __init__(self,name,age , id , sallary):
        self.id=id
        self.sallary = sallary
        person.__init__(self,name , age)
    def PrintDetails (self):
        print(f"my sallary is {self.sallary} , my id is {self.id} ")