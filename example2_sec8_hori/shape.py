from enum import Enum


class ShapeType(Enum):
    LINE = 0
    RECTANGLE = 1
    OVAL = 2


class Shape:

    def __init__(self, startx, starty, endx, endy):
        self._startx = startx
        self._starty = starty
        self._endx = endx
        self._endy = endy

    def name(self):
        pass

    def draw(self):
        pass

    def __str__(self):
        return '[' + self.name() + ', (' + str(self._startx) +  \
            ', ' + str(self._starty) + ')-' + '(' + str(self._endx) + \
            ', ' + str(self._endy) + ') ]'


class Line(Shape):

    def __init__(self, startx, starty, endx, endy):
        super().__init__(startx, starty, endx, endy)

    def name(self):
        return 'LINE'

    def draw(self):
        print('draw_line:{}'.format(str(self)))


class Rectangle(Shape):

    def __init__(self, startx, starty, endx, endy):
        super().__init__(startx, starty, endx, endy)

    def name(self):
        return 'RECTANGLE'

    def draw(self):
        print('draw_rectangle:{}'.format(str(self)))


class Oval(Shape):

    def __init__(self, startx, starty, endx, endy):
        super().__init__(startx, starty, endx, endy)

    def name(self):
        return 'OVAL'

    def draw(self):
        print('draw_oval:{}'.format(str(self)))


class ShapeFactory:

    @classmethod
    def create(cls, shape_type, startx, starty, endx, endy):
        if ShapeType.LINE == shape_type:
            return Line(startx, starty, endx, endy)
        elif ShapeType.RECTANGLE == shape_type:
            return Rectangle(startx, starty, endx, endy)
        elif ShapeType.OVAL == shape_type:
            return Oval(startx, starty, endx, endy)
        else:
            raise Exception('no type error')
