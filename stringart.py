"""
String Art Library in Python.
"""

import numpy as np
from joy import circle, line, Group, Shape, scale, translate, rotate

class StringArt:
    POINT_COLOR = "#444"
    LINE_COLOR = "rgba(72, 26, 132, 0.8)"

    def __init__(self):
        self.reset()

    def reset(self):
        self.points = []
        self.lines = []
        self.labels = []

    def draw(self):
        points = [self._draw_point(x, y) for x, y in self.points]
        lines = [self._draw_line(p1, p2) for p1, p2 in self.lines]
        labels = [self._draw_label(x, y, text, angle) for x, y, text, angle in self.labels]
        return Group(points+lines+labels)

    def _draw_point(self, x, y):
        return circle(x=x, y=y, r=1, fill=self.POINT_COLOR)

    def _draw_line(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return line(x1=x1, y1=y1, x2=x2, y2=y2, stroke_width=0.5, stroke=self.LINE_COLOR)

    def _draw_label(self, x, y, label, angle):
        return self._text(0, 0, label) | scale(x=1, y=-1) | rotate(angle) | translate(x=x, y=y)

    def _repr_svg_(self):
        """Returns the svg representation of this node.

        This method is called by Juputer to render this object as an
        svg image.
        """
        img = self.draw()
        return img.as_svg()

    def make_circle(self, n):
        """Makes a circle with n points.
        """
        self.reset()
        t = -np.linspace(0, 2*np.pi, n, endpoint=False)+np.pi/2
        r = 120
        self.points = list(zip(r*np.cos(t), r*np.sin(t)))

        if n <= 36:
            r1 = r + 10
            labels = [str(i) for i in range(n)]
            self.labels = list(zip(r1*np.cos(t), r1* np.sin(t), labels, np.linspace(360, 0, n)))
        return self

    def connect(self, a, b):
        n = len(self.points)
        a = a % n
        b = b % n
        p1 = self.points[a]
        p2 = self.points[b]
        self.lines.append((p1, p2))
        return self

    def _text(self, x, y, content):
        kwargs = dict(
            style='font: normal 10px sans-serif;',
            text_anchor='middle',
            fill='#888',
            stroke='none')
        return Shape(tag="text", x=x, y=y,
                    children=[_Text(content)], **kwargs)

class _Text:
    def __init__(self, content):
        self.content = content
    def _svg(self, indent):
        return self.content

_art = StringArt()

def make_circle(n=36):
    """Makes a circle with n points.
    """
    return _art.make_circle(n)

def connect(a, b):
    """Connects point a and b.

    Usage:

        make_circle(5)
        connect(0, 1)
        connect(1, 5)
    """
    return _art.connect(a, b)

def show(art=None):
    from IPython.display import display
    art = art or _art
    display(art)
