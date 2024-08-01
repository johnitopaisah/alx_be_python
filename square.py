import matplotlib.pyplot as plt

#  Define the Point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#  Define the Square class
class Square:
    def __init__(self, bottom_left, side_length):
        self.bottom_left = bottom_left
        self.side_length = side_length
        self.points = self._calculate_points()

    def _calculate_points(self):
        """
            Calculate the four corners of the square 
            based on the bottom-left corner and side 
            length
        """
        bl = self.bottom_left
        sl = self.side_length
        # Calculate the other three points based on the bottom-left points
        return [
            bl,
            Point(2*bl.x + sl, bl.y),         # bottom-right
            Point(bl.x + sl, bl.y + sl),    # top-ritht
            Point(2*bl.x, bl.y + sl)          # top-left
        ]
    
    

    def draw(self):
        """Draw teh square using matplotlib."""
        x_values = [p.x for p in self.points] + [self.points[0].x]
        y_values = [p.y for p in self.points] + [self.points[0].y]

        plt.plot(x_values, y_values, 'bo-')     # 'bo-' for blue color, curcle marker, and solid line
        plt.fill(x_values, y_values, 'skyblue', alpha=0.3) # Fill the square with a light blue color
        plt.title("Square")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid("True")
        plt.axis("equal")
        plt.show()

# Usage
bottom_left_point = Point(2, 3)         # Bottom-left corner at (1, 1)
side_length = 4                         # Side of the square
square = Square(bottom_left_point, side_length)
square.draw()