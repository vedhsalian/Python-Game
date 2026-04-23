from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        """Must be implemented by subclasses"""
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def description(self):
        """Concrete method shared by all subclasses"""
        print("This is a geometric shape.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)
    
    def perimeter(self):
        return 2*3.14*self.radius
    
class Square(Shape):
    def __init__(self,side):
        self.side=side
    
    def area(self):
        return self.side**2
    
    def perimeter(self):
        return self.side*4

#my_shape = Shape()# Raises TypeError
#my_shape.description()

my_circle = Circle(5)
#print(my_circle.area()) # 78.5
my_circle.description() # This is a geometric shape.

square=Square(4)

print(square.perimeter())