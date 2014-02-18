

difference() {
	difference() {
		union() {
			difference() {
				cylinder(h = 34, r = 6);
				translate(v = [0, 0, -0.1000000000]) {
					cylinder(r1 = 3.6000000000, r2 = 0.9000000000, h = 3);
				}
			}
			translate(v = [0, 0, 34]) {
				cylinder(r1 = 3, r2 = 1.8000000000, h = 1);
			}
		}
		cylinder(h = 36, r = 1.2000000000);
	}
	translate(v = [0, -1.2000000000, 0]) {
		translate(v = [0, 0, 25]) {
			cube(size = [6, 2.4000000000, 11]);
		}
	}
}
/***********************************************
******      SolidPython code:      *************
************************************************
 
#! /usr/bin/python

from solid import *
from solid.utils import *  # Not required, but the utils module is useful

scad_file = 'segment.py.scad'

# Segment body
segment_h = 34
segment_r = 6
body = cylinder (r = segment_r,
                 h = segment_h)

# Upper cone
cone_upper_h = 1
cone_upper_r1 = 3
cone_upper_r2 = 1.8
cone_upper = cylinder (r1 = cone_upper_r1,
                       r2 = cone_upper_r2,
                       h = cone_upper_h)

#Lower cone
cone_lower_h = 3
cone_lower_r1 = 3.6
cone_lower_r2 = 0.9
cone_lower = cylinder (r1 = cone_lower_r1,
                       r2 = cone_lower_r2,
                       h = cone_lower_h)

# Central hole
hole_r = 2.4/2
hole_h = segment_h + cone_upper_h + 1
hole = cylinder (r = hole_r,
                 h = hole_h)

# Slit
slit_h = 10   # height without upper cone height
slit_w = hole_r * 2

slit = cube([segment_r, slit_w, slit_h + cone_upper_h])


d = (((body - down(0.1)(cone_lower))
      + up(34)(cone_upper))
     - hole
     - back(slit_w / 2) (up (segment_h + cone_upper_h - slit_h) (slit)))

scad_render_to_file(d, scad_file)
 
 
***********************************************/
                            
