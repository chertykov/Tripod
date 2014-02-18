
all: segment.py.scad balljoint-test.py.scad

segment.py.scad : segment.py
	python segment.py

balljoint-test.py.scad : balljoint-test.py
	python $< > $@


