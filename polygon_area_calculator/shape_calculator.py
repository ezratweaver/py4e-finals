class Rectangle():

    def __init__(self, width, height):
        self.set_width(width)
        self.set_height(height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            row = "*" * self.width
            row = row + "\n"
            picture = picture + row
        return picture

    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())


class Square(Rectangle):

    def __init__(self, side):
        self.side = side
        self.set_side(side)

    def __str__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_height(self, height):
        self.side = height

    def set_width(self, width):
        self.side = width
