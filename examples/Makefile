EXAMPLES := $(filter-out _%.py,$(wildcard *.py))
SVGS := $(EXAMPLES:.py=.svg)

all: $(SVGS)

%.svg: %.py _build.py ../stringart.py
	uv run python _build.py $< $@

clean:
	rm -f $(SVGS)

.PHONY: all clean
