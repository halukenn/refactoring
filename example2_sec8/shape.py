class Shape:

    TYPECODE_LINE = 0
    TYPECODE_RECTANGLE = 1
    TYPECODE_OVAL = 2

    def __init__(self, typecode, startx, starty, endx, endy):
        self._typecode = typecode
        self._startx = startx
        self._starty = starty
        self._endx = endx
        self._endy = endy

    def get_typecode(self):
        return self._typecode

    def get_name(self):
        if self._typecode == self.TYPECODE_LINE:
            return 'LINE'
        elif self._typecode == self.TYPECODE_RECTANGLE:
            return 'RECTANGLE'
        elif self._typecode == self.TYPECODE_OVAL:
            return 'OVAL'
        else:
            return None

    def __str__(self):
        return '[' + self.get_name() + ', (' + str(self._startx) +  \
            ', ' + str(self._starty) + ')-' + '(' + str(self._endx) + \
            ', ' + str(self._endy) + ') ]'

    def draw(self):
        if self._typecode == self.TYPECODE_LINE:
            return self.draw_line()
        elif self._typecode == self.TYPECODE_RECTANGLE:
            return self.draw_rectangle()
        elif self._typecode == self.TYPECODE_OVAL:
            return self.draw_oval()
        else:
            return None

    def draw_line(self):
        print('draw_line:{}'.format(str(self)))

    def draw_rectangle(self):
        print('draw_rectangle:{}'.format(str(self)))

    def draw_oval(self):
        print('draw_oval:{}'.format(str(self)))
