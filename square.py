class Square:
    def __init__(self, square_side:float):
        self.square_side = square_side
    
    def is_valid(self) -> bool:
        """
        This method checks if the circle is valid.
        Args:
            No
        Returns:
            bool: This method checks if the square is valid.
        """
        return self.square_side>0

    def area(self) -> float:
        """
        This method finds the area of the square.
        Args:
            No
        Returns:
            float or int: return area of the square if the square is valid, 0 otherwise
        """
        return self.square_side**2 if square.is_valid() else 0

    def perimeter(self) -> float:
        """
        This method finds the perimeter of the square.
        Args:
            No
        Returns:
            float: return perimeter of the square if the square is valid, 0 otherwise
        """
        return self.square_side*4 if square.is_valid() else 0

square = Square(6)
is_valid_square = square.is_valid()
square_perimeter = square.perimeter()
square_area = square.area()

print("Can it be a square?", is_valid_square)
# Can it be a square? True
print("The perimeter of the square is:", square_perimeter)
# The perimeter of the square is: 24
print("The area of the square is:", square_area)
# The area of the square is: 36