class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"

class Circle:
    def __str__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius