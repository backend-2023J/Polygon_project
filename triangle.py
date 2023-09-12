from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        return self.a+self.b>self.c and self.a+self.c>self.a and self.b+self.c > self.a 
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        if triangle1.is_valid() == True:
            if self.a == self.b == self.c:
                return "Teng tomonli"
            elif self.a == self.b or self.a == self.c or self.b == self.c:
                return "Teng yonli"
            return "Turli tomonli"
        return 0
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        return self.a+self.b+self.c if triangle1.is_valid() else 0

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        s = triangle1.perimeter()/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5 if triangle1.is_valid() else 0

triangle1 = Triangle(3.0, 4.0, 5.0)

print("Can it be a triangle?", triangle1.is_valid())
# Can it be a triangle? True
print("Type of trianle:", triangle1.get_type())
# Type of triangle: Turli tomonli
print("The perimeter of the triangle is:", triangle1.perimeter())
# The perimeter of the triangle is: 12.0
print("The area of the triangle is:", triangle1.area())
# The area of the triangle is: 6.0