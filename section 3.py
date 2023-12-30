import os 
os.system("cls")

class customer :
    def SetName(self,name):
        self.name = name
    def PrintData (self):
        print (f"your name : {self.name}")

ahmed = customer()
ahmed.SetName("ahmed")
ahmed.PrintData()

ahmed.anothername = "mohamed"
print (ahmed.anothername)

# isinstance 
## return if object in class or not (true)
print(isinstance (ahmed,customer))


# modifier ( 1 : public , 2 : protected , 3 : private )
# private __before attruibute name , protected _before attruibute name

# protected 
## can get in main class
## can get again in extends class if class inhertance main class
## in global scope we can get by setter and getter methods

# private 
## can get in main class

class person ():
    attr1 = "public" # public attruibute
    _attr2 = "protected" # protected attruibute
    __attr3 = "private" # private attruibute

    def __init__ (self):
        print (self.attr1)
        print (self._attr2) # this access protected attruibute
        print (self.__attr3) # this access private attruibute (" main class only ")
    def display_name (self):
        print (self.__attr3)  # this access private attruibute (" main class only ")

class ahmed (person):
    def display (self):
        print (self._attr2)  # this access protected attruibute

a = ahmed ()
a.display() # this access protected attruibute
a.display_name() # this access private attruibute



