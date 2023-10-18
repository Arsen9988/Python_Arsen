import math
class Shapes:
    def __init__(self, x: float, y: float):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)): # error-handling
            raise TypeError("x and/or y is NOT int or float values") 
        self.x = x
        self.y = y
    @property
    def area(self):
        return 0 # will be used in child classes
    @property
    def perimeter(self):
        return 0 # will be used in child classes
    def __eq__(self, other):
        return f'{self.area = },  {other.area = }', self.area == other.area
    def __lt__(self, other):
        return self.area < other.area
    def __gt__(self, other):
        return self.area > other.area
    def __le__(self, other):
        return self.area <= other.area
    def __ge__(self, other):
        return self.area >= other.area
    def translate(self, new_x: float, new_y: float):
        if not isinstance(new_x, (int, float)) or not isinstance(new_y, (int, float)): # error-handling
            raise TypeError("new_x and/or new_y is NOT int or float values")
        self.x = new_x
        self.y = new_y
    def __str__(self): # General __str__() for all types of classes 
        return f'{self.__class__.__name__}: center = ({self.x}, {self.y}) | Area = {self.area:.2f} | Perimeter = {self.perimeter:.2f}'
        
class Rectangle(Shapes):
    def __init__(self, x, y, width: float, height: float):
        super().__init__(x, y)
        assert width > 0, f'Width: ({width}) is NOT greater than zero!'
        assert height > 0, f'Height: ({height}) is NOT greater than zero!'
        self._width = width
        self._height = height
    @property
    def area(self):
        return float(self._width * self._height)
    @property
    def perimeter(self):
        return float(2 * self._width + 2 * self._height)
    def is_inside(self, x1, y1):
        x_min = self.x - (self._width / 2)
        x_max = self.x + (self._width / 2)
        y_min = self.y - (self._height / 2)
        y_max = self.y + (self._height / 2)   
        if x_min <= x1 <= x_max and y_min <= y1 <= y_max :
            return f'({x1}, {y1}) is inside {self.__class__.__name__}'
        else:
           return f'({x1}, {y1}) is NOT inside {self.__class__.__name__}'
    def is_square(self):
        if self._width == self._height:
            return True
        else:
            return False
    def __repr__(self): # More detailed representation than in __str__
        return f'{self.__class__.__name__ = } | {self.x = }, {self.y = } | {self.area = } | {self._width = }, {self._height = }'
    
class Circle(Shapes):
    def __init__(self, x, y, radius: float):
        super().__init__(x, y)
        if not isinstance(radius, (int, float)): # error-handling
            raise TypeError(f"Radius: ({radius}) is NOT int or float value")
        assert radius > 0, f'Radius: ({radius}) is NOT greater than zero!' # Assersion makes in impossible to make (-value) radius
        self._radius = radius
    @property
    def area(self):
        return float(math.pi * self._radius**2)
    @property
    def perimeter(self):
        return float(2 * math.pi * self._radius)
    def is_inside(self, x1, y1):
        distance = math.sqrt((x1 - self.x)**2 + (y1 - self.y)**2)
        if distance <= self._radius:
            return f'({x1}, {y1}) is inside {self.__class__.__name__}'
        else:
           return f'({x1}, {y1}) is NOT inside {self.__class__.__name__}'
    def is_unit_circle(self):
        if self.x == 0 and self.y == 0 and self._radius == 1: # Unit circle parameters
            return True
        else:
            return False
    def __repr__(self):  # More detailed representation than __str__
        return f'{self.__class__.__name__ = } | {self.x = }, {self.y = } | {self.area = } | {self._radius = }'