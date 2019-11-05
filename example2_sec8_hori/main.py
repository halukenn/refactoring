from shape import ShapeFactory
from shape import ShapeType


def execute():
    line = ShapeFactory.create(ShapeType.LINE, 0, 0, 100, 200)
    rectangle = ShapeFactory.create(ShapeType.RECTANGLE, 10, 20, 30, 40)
    oval = ShapeFactory.create(ShapeType.OVAL, 100, 200, 300, 400)

    shapes = [line, rectangle, oval]
    for shape in shapes:
        shape.draw()


if __name__ == "__main__":
    execute()
