class C1:
    V1 = "class attribute "
    def __init__(self , V2 ):
        self.V2 = V2 # instance attribute
    def display (self):
        print ( ahmed.V1) # can access the class attribute
    def edit (self , V2 ):
        self.V2 = V2
    def display2 (self):
        print (self.V2)

a=C1("instance attribute ") # this create instance attribute
a.display() # access class attribute
a.V1 = 9 # edit class attribute to 9

a.display2() # access instance attribute
a.edit(5) # edit instance attribute to 5 
a.display2() # access instance attribute


## overloading
def add (Datatype , *args):
    if Datatype == int:
        sum = 0
    else :
        sum = ""

    for i in args :
        sum+=i
    print (sum)

add(int,1,5,7,9)
add(str,"ahmed " , "mohamed")


def product (a = "none" , b = "none") :
    if b == "none":
        return a
    else :
        return a*b
c = product (1)
print(c)

from multipledispatch import dispatch

@dispatch (int , int )
def ahmed (a1 , a2 ):
    print (a1*a2)

@dispatch (int , int , int)
def ahmed (a1 , a2 , a3  ):
    print (a1*a2*a3)

ahmed (1,2)
ahmed(4,2,3)