## continue ==> ignore condition 
for i in range (10):
    if i == 5:
        continue
    else :
       print (i)

## pass ==> return value instead of condition
for i in range (10):
    if i == 5:
        pass 
        print("ahmed")
    else :
       print (i )

## break ==> stop loop when condition 
for i in range (10):
    if i == 5 :
        break
    else :
        print(i)

## while Loop
i=1
while (i<10):
    print (i)
    i=i+1

## function

def ahmed (x):
    for i in range (x):
        print (i)
ahmed(4)

def sum (x,y):
    return(x+y)
a = sum(1,3)
print(a)


## funcution as referance ( paramter )
def product (n1,n2):
    print (n1*n2)
def function ( func , n1 , n2 ):
    func(n1,n2)
function(product , 5 , 10)

## function in function
def func1(name,age):
    print (f" my name is {name}")
    def func2 (age):
        print (f" my age is {age}")
    func2(age)
func1("ahmed" , 19)


## defult argument in funcution
def func3 (x, a = "none", b = "none" ):
    """this funcution has defult valie of a , b .... we can return x+a+b or x+a or x+b"""
    if (a == "none"):
        return x+b
    elif( b== "none"):
        return x+a
    else :
        return x+a+b
    
help(func3) 
func3(1,2,3)
func3(1,2)
func3(1, b=5)
