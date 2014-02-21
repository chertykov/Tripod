
all: segment.scad balljoint-test.scad plate.scad clamp.scad
%.scad: %.py
	python $< > $@

