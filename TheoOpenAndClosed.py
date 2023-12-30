class Shape:
  def area(self):
   pass

class Rectangle(Shape):
  def init_(self, width, height):
        self.width = width
        self.height = height

def area(self):
    return self.width * self.height

class Circle(Shape):
    def _init_(self, radius):
       self.radius = radius

def area(self):
    return 3.14 * self.radius * self.radius


class Triangle(Shape):
   def _init_(self, base, height):
     self.base = base
     self.height = height

def area(self):
   return 0.5 * self.base * self.height