## abstract method
# funcution withoutbody in class

from abc import ABC , abstractmethod
class ahmed (ABC):
    @abstractmethod
    def func (self , name ):
        pass
class hassan (ahmed):
    def func(self , name ):
        print (f"my name is {name}")

a = hassan ()
a.func("ahmed")