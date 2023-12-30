import os 
os.system("cls")

#__ this make variable private
#__len__ بيجيب عدد العناصر

from collections.abc import Sequence
class item (Sequence):
    def __init__ (self , *a ) :
        sum = 0 
        self.a = list(a)
        for i in a:
            sum = int(i)+sum
        print (sum)

    def __len__ (self):
         print( len (self.a))

    def __getitem__ (self,item):
         print( self.a.__getitem__ (item))
    
ahmed = item (1,5,7,8,9,7,5,2,6)
ahmed.__len__()
ahmed.__getitem__(5)