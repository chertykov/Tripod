
all: segment.scad balljoint-test.scad plate.scad clamp.scad phone-mount.scad

%.scad: %.py
	python $< > $@

plate.scad: plate.py segment.py

clamp.scad: plate.py clamp.py

phone-mount.scad: plate.py phone-mount.py
