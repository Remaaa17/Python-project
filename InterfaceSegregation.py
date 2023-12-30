from abc import ABC, abstractmethod

class Shape(ABC):
 @abstractmethod
 def area(self):
      pass

 @abstractmethod
 def perimeter(self):
  pass

class Rectangle(Shape):
  def _init_(self, width, height):
    self.width = width
    self.height = height

  def area(self):
   return self.width * self.height

  def perimeter(self):
    return 2 * (self.width + self.height)

##############################
from abc import ABC, abstractmethod

# Bad Example
class Shape(ABC):
 @abstractmethod
 def area(self):
  pass

 @abstractmethod
 def perimeter(self):
  pass

class Circle(Shape):
   def _init_(self, radius):
        self.radius = radius

   def area(self):
         return 3.14 * self.radius * self.radius

   def perimeter(self):
      return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def _init_(self, width, height):
         self.width = width
         self.height = height

    def area(self):
       return self.width * self.height

    def perimeter(self):
       return 2 * (self.width + self.height)

###########################################
from abc import ABC, abstractmethod

# Good Example
class AreaCalculatable(ABC):
 @abstractmethod
 def calculate_area(self):
  pass
class PerimeterCalculatable(ABC):
 @abstractmethod
 def calculate_perimeter(self):
   pass

class Circle(AreaCalculatable, PerimeterCalculatable):
   def _init_(self, radius):
     self.radius = radius

   def calculate_area(self):
     return 3.14 * self.radius * self.radius

   def calculate_perimeter(self):
      return 2 * 3.14 * self.radius

class Rectangle(AreaCalculatable, PerimeterCalculatable):
     def _init_(self, width, height):
          self.width = width
          self.height = height

     def calculate_area(self):
          return self.width * self.height

     def calculate_perimeter(self):
          return 2 * (self.width + self.height)
#########################################################
from abc import ABC, abstractmethod
from typing import Protocol
# Define an interface for printable objects
class Printable(Protocol):
 @abstractmethod
 def print(self) -> None:
   pass
# Define an interface for scannable objects
class Scannable(Protocol):
 @abstractmethod
 def scan(self) -> None:
   pass
# Define an interface for faxable objects
class Faxable(Protocol):
 @abstractmethod
 def fax(self) -> None:
   pass
# Define a class that implements the Printable interface
class Document(Printable):
 def __init__(self, content: str):
      self.content = content
 # Implement the print method
 def print(self) -> None:
   print(self.content)

# Define a class that implements the Scannable and Faxable interfaces
class Image(Scannable, Faxable):
 def __init__(self, data: bytes):
      self.data = data
 # Implement the scan method
 def scan(self) -> None:
   print("Scanning the image")
 # Implement the fax method
 def fax(self) -> None:
  print("Faxing the image")
# Define a class that depends on the Printable interface
class Printer:
 def print(self, printable: Printable) -> None:
 # Use the print method of the printable object
   printable.print()
# Define a class that depends on the Scannable and Faxable interfaces
class ScannerFaxer:
 def scan_and_fax(self, scannable: Scannable,faxable: Faxable) -> None:
 # Use the scan method of the scannable object
   scannable.scan()
 # Use the fax method of the faxable object
   faxable.fax()
# Create a document object
document = Document("Hello, world!")
# Create an image object
image = Image(b"\x89PNG\r\n\x1a\n\x00\x00")
# Create a printer object
printer = Printer()
# Print the document using the printer
printer.print(document)
# Create a scanner-faxer object
scanner_faxer = ScannerFaxer()
# Scan and fax the image using the scanner-faxer
scanner_faxer.scan_and_fax(image, image)


