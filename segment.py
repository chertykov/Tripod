#! /usr/bin/python

from solid import *
from solid.utils import *  # Not required, but the utils module is useful

# Segment body
segment_h = 34.0
segment_r = 6.0
body = cylinder (r = segment_r,
                 h = segment_h)

# Upper cone
cone_upper_h = 1.0
cone_upper_r1 = 3.3
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
slit_h = segment_r * 2 * 0.85   # slit height without upper cone height
slit_w = hole_r * 1.7

slit = cube([segment_r + 1, slit_w, slit_h + cone_upper_h])


segment = (body
	   - down(0.1)(cone_lower)
	   + up(segment_h)(cone_upper)
           - hole
           - back(slit_w / 2) (up (segment_h + cone_upper_h - slit_h) (slit)))

if __name__ == "__main__":
    # Render quality
    print '$fn=32;'
    print scad_render(segment)
