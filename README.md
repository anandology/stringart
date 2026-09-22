# String Art

A Python library to explore string art.

<img src="https://raw.githubusercontent.com/anandology/stringart/main/examples/three-circles.svg" width="300" alt="String art with three layers of threads">

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
| [![](https://raw.githubusercontent.com/anandology/stringart/main/examples/pentagon.svg)](examples/pentagon.py) | [![](https://raw.githubusercontent.com/anandology/stringart/main/examples/pentagonal-star.svg)](examples/pentagonal-star.py) | [![](https://raw.githubusercontent.com/anandology/stringart/main/examples/radials.svg)](examples/radials.py) |
| [pentagon.py](examples/pentagon.py) | [pentagonal-star.py](examples/pentagonal-star.py) | [radials.py](examples/radials.py) |

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
