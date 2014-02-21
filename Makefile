
all: segment.scad balljoint-test.scad plate.scad clamp.scad

%.scad: %.py
	python $< > $@

plate.scad: plate.py segment.py

