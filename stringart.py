"""
String Art Library in Python.
"""

import numpy as np
from joy import circle, line, Group, Shape, scale, translate

class StringArt:
    RADIUS = 120
    LINE_COLOR = "#c2185b"
    POINT_COLOR = "#3e2f24"
    POINT_OUTLINE_COLOR = "#fffaf2"
    LABEL_COLOR = "#9a8a78"
    BACKGROUND_COLOR = "#f3ebdd"
    BORDER_COLOR = "#d8cbb8"
    GUIDE_COLOR = "#c9b79c"

    def __init__(self):
        self.reset()
        self.line_color = self.LINE_COLOR
        self.stroke_width = 1.1

    def reset(self):
        self.points = []
        self.lines = []
        self.labels = []

    def set_color(self, color):
        self.line_color = color

    def draw(self):
        background = circle(r=148, fill=self.BACKGROUND_COLOR,
                            stroke=self.BORDER_COLOR, stroke_width=1)
        guide = circle(r=self.RADIUS, fill="none", stroke=self.GUIDE_COLOR,
                       stroke_width=0.75, stroke_dasharray="2 3")

        lines = Group(
            [self._draw_line(p1, p2, color) for p1, p2, color in self.lines],
            stroke_width=self.stroke_width,
            stroke_linecap="round")
        points = Group(
            [self._draw_point(i, x, y) for i, (x, y) in enumerate(self.points)],
            fill=self.POINT_COLOR,
            stroke=self.POINT_OUTLINE_COLOR,
            stroke_width=1)
        labels = Group(
            [self._draw_label(x, y, text) for x, y, text in self.labels],
            font_family="ui-monospace, 'JetBrains Mono', Menlo, Consolas, monospace",
            font_size=9,
            fill=self.LABEL_COLOR,
            stroke="none",
            text_anchor="middle")
        return Group([background, guide, lines, points, labels])

    def _draw_point(self, index, x, y):
        # the starting point is drawn bigger to make it easy to spot
        r = 3.2 if index == 0 else 2.4
        return circle(x=x, y=y, r=r)

    def _draw_line(self, p1, p2, color):
        x1, y1 = p1
        x2, y2 = p2
        return line(x1=x1, y1=y1, x2=x2, y2=y2, stroke=color)

    def _draw_label(self, x, y, label):
        weight = "700" if label == "0" else None
        return self._text(0, 0, label, font_weight=weight, dominant_baseline="central") | scale(x=1, y=-1) | translate(x=x, y=y)

    def _repr_svg_(self):
        """Returns the svg representation of this node.

        This method is called by Juputer to render this object as an
        svg image.
        """
        return self.as_svg()

    def as_svg(self):
        """Returns the svg representation of this string art as a string.
        """
        return self.draw().as_svg()

    def save(self, path):
        """Saves this string art as an svg file.
        """
        with open(path, "w") as f:
            f.write(self.as_svg())

    def make_circle(self, n):
        """Makes a circle with n points.
        """
        self.reset()
        t = -np.linspace(0, 2*np.pi, n, endpoint=False)+np.pi/2
        r = self.RADIUS
        self.points = list(zip(r*np.cos(t), r*np.sin(t)))

        num_labels = self._find_num_labels(n)
        if not num_labels:
            self.labels = []
        else:
            step = n // num_labels
            r1 = r + 12
            labels = [str(i) for i in range(0, n, step)]
            tt = t[::step]
            self.labels = list(zip(r1*np.cos(tt), r1*np.sin(tt), labels))

        return self

    def _find_num_labels(self, n):
        if n <= 30:
            return n
        elif n%2 == 0 and n <= 40:
            return n//2
        elif n%3 == 0 and n <= 60:
            return n//3
        elif n%4 == 0 and n <= 80:
            return n//4
        elif n%5 == 0 and n <= 100:
            return n//5
        else:
            # no labels
            return 0



    def connect(self, a, b):
        n = len(self.points)
        a = a % n
        b = b % n
        p1 = self.points[a]
        p2 = self.points[b]
        self.lines.append((p1, p2, self.line_color))
        return self

    def _text(self, x, y, content, **kwargs):
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

def set_color(color):
    return _art.set_color(color)

def save(path, art=None):
    """Saves the string art as an svg file.

    Usage:

        make_circle(10)
        connect(0, 5)
        save("art.svg")
    """
    art = art or _art
    art.save(path)

def show(art=None):
    from IPython.display import display
    art = art or _art
    display(art)
