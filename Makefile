
all: segment.py.scad balljoint-test.py.scad plate.py.scad

segment.py.scad : segment.py
	python segment.py

balljoint-test.py.scad : balljoint-test.py
	python $< > $@

plate.py.scad : plate.py
	python $< > $@


