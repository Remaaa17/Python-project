##interface##
import zope.interface
# Define an interface 'Printable' that has a method 'format'
class Printable(zope.interface.Interface):
 def format(self):
  pass
# Define a class 'Book' that implements the 'Printable' interface
@zope.interface.implementer(Printable)
class Book:
 def __init__(self, title, author, content):
    self.title = title
    self.author = author
    self.content = content
 # Implement the 'format' method to return the book's content
 def format(self):
   return f"{self.title} by {self.author}\n{self.content}"
# Define a class 'Printer' that depends on the 'Printable' interface
class Printer:
 def print(self, printable):##Use the 'format' method of the printable object
  formatted_content = printable.format()
  print(formatted_content)
# Create a book object
book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Don't Panic.")
# Create a printer object
printer = Printer()
# Print the book using the printer
printer.print(book)

###############################################
##abstract class##
from abc import ABC, abstractmethod
# Define an abstract base class 'Shape'
class Shape(ABC):
 @abstractmethod
 def area(self):
  pass
# Define a class 'Circle' that inherits from 'Shape'
class Circle(Shape):
 def __init__(self, radius):
   self.radius = radius
 # Implement the abstract method 'area'
 def area(self):
   return 3.14159 * self.radius ** 2
# Define a class 'Rectangle' that inherits from 'Shape'
class Rectangle(Shape):
 def __init__(self, width, length):
    self.width = width
    self.length = length
 # Implement the abstract method 'area'
 def area(self):
    return self.width * self.length
# Create instances of 'Circle' and 'Rectangle'
circle = Circle(4)
rectangle = Rectangle(5, 7)
# Calculate and print the area of the shapes
print(circle.area()) # Output: 50.26544
print(rectangle.area()) # Output: 35