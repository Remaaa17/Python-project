# A superclass that represents animals
class Animal:
 def make_sound(self):
   pass
# A subclass that represents dogs
class Dog(Animal):
 def make_sound(self):
   print("Woof")
# A subclass that represents cats
class Cat(Animal):
 def make_sound(self):
   print("Meow")
# A function that accepts an animal object and calls its make_sound method
def play_with_animal(animal):
 animal.make_sound()
# Create a dog object and a cat object
dog = Dog()
cat = Cat()
# Pass the dog and cat objects to the function
play_with_animal(dog) # prints "Woof"
play_with_animal(cat) # prints "Meow"

################################################
class Rectangle:
 def _init_(self, width, height):
  self.width = width
  self.height = height

def set_width(self, width):
  self.width = width

def set_height(self, height):
  self.height = height

def get_area(self):
   return self.width * self.height

class Square(Rectangle):
    def set_width(self, width):
       self.width = width
       self.height = width

    def set_height(self, height):
         self.width = height
         self.height = height

    def print_area(rectangle):
       rectangle.set_width(4)
       rectangle.set_height(5)
       area = rectangle.get_area()
       print(f"The area is: {area}")

rectangle = Rectangle(3, 4)
square = Square(5)
print_area(rectangle)  # Output: The area is: 20
print_area(square)  # Unexpected output: The area is: 25 (Incorrect!)