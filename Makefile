
all: segment.scad balljoint-test.scad plate.scad clamp.scad

segment.scad : segment.py
	python segment.py

balljoint-test.scad : balljoint-test.py
	python $< > $@

plate.scad : plate.py
	python $< > $@

clamp.scad : clamp.py
	python $< > $@
