import os 
os.system("cls")

## every object has type , data representation ,  .... object ==> instance
## every thing in python is object 
## object is a data abstraction that capture ( internal representation , interface )

## list is maniplulate قابله للتعديل
## in list we can use 
### L[i], L[i:j] ==> "slicing"
### len() ==> عدد العناصر, min() ==> اقل قيمه , max() ==> اكبر قيمه , del(L[i]) ==> امسح عنصر فيها
### L.append() ==> بيضيف عنصر في الاخر , L.insert(index , element) ==> بيضيف عنصر في الرقم اللي انا عايزه , L.extend() ==>  بيضيف قم list تانيه في قلب دي  
### L.pop() ==> بيحذف رقم بالindex , L.remove(element) ==> بيحذف عنصر بالاسم , L.reverse() ==> بيعكس الترتيب , L.sort() ==> بيرتبها 
### L.count(i) ==> بيعد عدد العنصر اللي حطيته  , L.index(i) ==> بيجيب رقم العنصر 

# OOP advantage 
## bundle date in backage
## easy to reuse code
## inheritance is allowed

# variables 
## class variable ( variable in class when create it " attributes " ) to use (classname.VName )
## instance variable ( variable in __init__ & but before it self.)
### isinstance(object , classname) ++> check if object in classname 

class ahmed:
    ahmed = 0 # attribuite
    def __init__ (self,n1,n2,n3=0): # special method
        self.n1=n1 # instance variable 
        self.n2=n2
        self.n3=n3
    def sum(self): # method
        return self.n1+self.n2+self.n3

a = ahmed (1,2,9)
b = ahmed (1,2)
# "." operator used to access any attribute
a.sum()
b.sum()

# we can destory object by del () and the name is garbage collection
# del(a)

print(isinstance(a,ahmed))
## special method
# __init__ ==> autmatic run when create object 
# __str__ ==> it run when print object 
# __add__ ==> when use Obj in sum opperation we control on it when add it
# __sub__ ==> when use Obj in - opperation we control on it when - it
# __eq__(self, other) ==> self == other
# __lt__(self, other) ==> self < other
# __len__(self) ==> len(self)

# FRACTIONS ==> 5/2

# oop power 
## bundle together objects that share (common attributes ,  procedures اجراءات , abstraction )