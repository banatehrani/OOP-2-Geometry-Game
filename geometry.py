class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class GuiPoint(Point):

    def draw(self, canvas, size=5, color='red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)


class Rectangle:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return abs((self.point2.x - self.point1.x) *
                   (self.point2.y - self.point1.y))


class GuiRectangle(Rectangle):

    def draw(self, canvas):
        # Go to a certain coordinate
        canvas.penup()  # Don't touch the canvas
        canvas.goto(self.point1.x, self.point1.y)

        canvas.pendown()  # Put the pen down for drawing
        canvas.forward(self.point2.x - self.point1.x)  # Move forward a specific number of pixels
        canvas.left(90)  # Turn left
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
