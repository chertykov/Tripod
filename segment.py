#! /usr/bin/python

from solid import *
from solid.utils import *  # Not required, but the utils module is useful

scad_file = 'segment.py.scad'

# Segment body
segment_h = 34.0
segment_r = 6.0
body = cylinder (r = segment_r,
                 h = segment_h)

# Upper cone
cone_upper_h = 1.0
cone_upper_r1 = 3.0
cone_upper_r2 = 1.8
cone_upper = cylinder (r1 = cone_upper_r1,
                       r2 = cone_upper_r2,
                       h = cone_upper_h)

#Lower cone
cone_lower_h = 3.0
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
slit_h = 10.0   # height without upper cone height
slit_w = hole_r * 2

slit = cube([segment_r, slit_w, slit_h + cone_upper_h])


d = (((body - down(0.1)(cone_lower))
      + up(34)(cone_upper))
     - hole
     - back(slit_w / 2) (up (segment_h + cone_upper_h - slit_h) (slit)))

scad_render_to_file(d, scad_file)
