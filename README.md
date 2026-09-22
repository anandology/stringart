# String Art

A tiny Python library for making string art, designed for teaching programming to beginners.

<img src="https://raw.githubusercontent.com/anandology/stringart/main/examples/three-circles.svg" width="300" alt="String art with three layers of threads">


## What is String Art

String art is a craft of making patterns by connecting points with a thread, typically around a circle. Each thread is a straight line, yet together they form curves and intricate patterns.

It grew out of *curve stitching*, a technique [Mary Everest Boole][1] developed in the late 1800s to help children explore geometry by sewing lines on cards.

<img src="https://raw.githubusercontent.com/anandology/stringart/main/images/four-circles.png" width="300" alt="String art with four layers of threads">

*Made by hand on a laser-cut card stock board.*

[1]: https://en.wikipedia.org/wiki/Mary_Everest_Boole

## Install

```
pip install stringart
```

Requires Python 3.9 or later.

## Quick Start

```python
from stringart import *

make_circle(18)

for i in range(18):
    connect(i, i+6)

show()
```

<img src="https://raw.githubusercontent.com/anandology/stringart/main/examples/circle.svg" width="300" alt="18 points, each connected to the point 6 steps ahead">

`show()` displays the art in a Jupyter notebook. In a plain Python script, use `save("art.svg")` to save it as an svg file instead.

## Functions

| Function | What it does |
|---|---|
| `make_circle(n)` | Starts a new art with `n` points on a circle, numbered `0` to `n-1`. |
| `connect(a, b)` | Connects point `a` to point `b` with a thread. |
| `show()` | Displays the art in Jupyter. |
| `save(path)` | Saves the art as an svg file. |

Point numbers wrap around the circle. With `18` points, `connect(17, 20)` is the same as `connect(17, 2)`. That is why `connect(i, i+6)` works for every `i` in the loop above.

## Examples

| | | |
|---|---|---|
| [![](https://raw.githubusercontent.com/anandology/stringart/main/examples/mystic-rose.svg)](examples/mystic-rose.py) | [![](https://raw.githubusercontent.com/anandology/stringart/main/examples/dewdrop.svg)](examples/dewdrop.py) | [![](https://raw.githubusercontent.com/anandology/stringart/main/examples/sunrise.svg)](examples/sunrise.py) |
| [mystic-rose.py](examples/mystic-rose.py) | [dewdrop.py](examples/dewdrop.py) | [sunrise.py](examples/sunrise.py) |

See the [examples](examples/) directory for the programs. To regenerate the svg files after changing them, run `make` in that directory.

## Why

StringArt was born out of a desire to teach programming to beginners in a fun, interactive way.

Every program draws a picture, so students see right away what their code does, and a mistake looks wrong instead of just printing a wrong number.

The API has just four functions, but the possible complexity is far from small. Connecting each point by hand quickly becomes tedious, and the need for a loop comes naturally. When the same pattern shows up again and again, the need for a function follows. Ideas like generalization and abstraction, which are hard to convey, emerge on their own in this medium.

## Development

```
uv sync
make -C examples
uv build
```

## License

MIT. See [LICENSE](LICENSE).
