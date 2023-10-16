

   # def __eq__(self, other):
    #     ...
    # def __lt__(self, other):
    #     ...
    # def __gt__(self, other):
    #     ...
    # def __le__(self, other):
    #     ...
    # def __ge__(self, other):
    #     ...
    
    # def __repr__(self):
    #     ...
    
    # def __str__(self):
    #     ...

    # def translate(self):
    #     ...
    # def is_inside(self):
    #     ...

import math
class Shapes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def area(self):
        return 0
        
    @property
    def perimeter(self):
        return 0
        
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Rectangle(Shapes):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return float(self._width * self._height)
    
    @property
    def perimeter(self):
        return float(2 * self._width + 2 * self._height)


#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Circle(Shapes):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self._radius = radius
    
    @property
    def area(self):
        return float(math.pi * self._radius**2)
    
    @property
    def perimeter(self):
        return float(2 * math.pi * self._radius)


print('******* Rektangel ***********')
rek = Rectangle(0, 0, 4, 2)
# print(f'{rek.area = }')
# print(f'{rek.perimeter = }')


print('\n******* Circle ***********')
cir = Circle(0, 0, math.sqrt(8/math.pi))
# print(f'{cir.area = }')   
# print(f'{cir.perimeter = }')




print(rek == cir)



# import math
# class Shapes:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     @property
#     def area(self):
#         return 0
        
#     @property
#     def perimeter(self):
#         return 0
        
#     def __eq__(self, other):
#         return f'{self.area = },  {other.area = }', self.area == other.area
    
#     def __str__(self):
#         return f'{self.__class__.__name__}: x,y = ({self.x}, {self.y}) | Area = {self.area}'
    
#     def translate(self, new_x, new_y):
#         self.x = new_x
#         self.y = new_y
        
# #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# class Rectangle(Shapes):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self._width = width
#         self._height = height
    
#     @property
#     def area(self):
#         return float(self._width * self._height)
    
#     @property
#     def perimeter(self):
#         return float(2 * self._width + 2 * self._height)
    
#     def is_inside(self, x1, y1):
#         x_min = self.x - (self._width / 2)
#         x_max = self.x + (self._width / 2)
#         y_min = self.y - (self._height / 2)
#         y_max = self.y + (self._height / 2)   
#         if x_min <= x1 <= x_max and y_min <= y1 <= y_max :
#             return f'({x1}, {y1}) is inside {self.__class__.__name__}'
#         else:
#            return f'({x1}, {y1}) is NOT inside {self.__class__.__name__}'
       
#     def is_square(self):
#         if self._width == self._height:
#             return True
#         else:
#             return False
            

        


# #'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# class Circle(Shapes):
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self._radius = radius
    
#     @property
#     def area(self):
#         return float(math.pi * self._radius**2)
    
#     @property
#     def perimeter(self):
#         return float(2 * math.pi * self._radius)

#     def is_inside(self, x1, y1):
#         distance = math.sqrt((x1 - self.x)**2 + (y1 - self.y)**2)
#         if distance <= self._radius:
#             return f'({x1}, {y1}) is inside {self.__class__.__name__}, {self._radius = }, {distance = }'
#         else:
#            return f'({x1}, {y1}) is NOT inside {self.__class__.__name__},  {self._radius = }, {distance = }'
    
#     def is_unit_circle(self):
#         if self.x == 0 and self.y == 0 and self._radius == 1:
#             return 'True'
#         else:
#             return 'False'
    


# #print('******* Rektangel ***********')
# rek = Rectangle(2, 1, 4, 2)

# rek2 = Rectangle(0,0,1,1)
# # print(f'{rek.area = }')
# # print(f'{rek.perimeter = }')


# #print('\n******* Circle ***********')
# cir = Circle(0, 0, math.sqrt(8/math.pi))
# cir2 = Circle(0, 0, 1)
# # print(f'{cir.area = }')   
# # print(f'{cir.perimeter = }')

