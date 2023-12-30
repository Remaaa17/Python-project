import os 
os.system("cls")

# def factorial (x):
#     n = int(x)
#     factorial = 1

#     for i in range (n , 1 , -1):
#         factorial=factorial*i
#     print ("the factorial of" , n , "=" , factorial )
# factorial(5)

def factorial (x):
    n = int(x)
    factorial = 1

    for i in range (n , 1 , -1):
        factorial=factorial*i
    return factorial

def c(n,r):
    new_fact3=factorial(n)
    new_fact=factorial(n-r)
    new_fact2=factorial(r)
    print (new_fact3/(new_fact*new_fact2))
c(5,3)

def p(n,r):
    print (factorial(n)/factorial(n-r))
p(5,3)

# x = int (input ("Enter your number : "))
# def func (x):
#     if x % 2 == 0:
#         print ("even")
#     else :
#         print ("odd")
# func(x)

### if we use more func by the same name we can use it by 
####  1. attributes 

# def sum (num1,num2, num3=None):
#     if num3==None:
#         print (num1+num2)
#     else:
#         print (num1+num2+num3)
# sum (1,2)
# sum (1,2,3)