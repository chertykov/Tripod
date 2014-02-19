#! /usr/bin/python

import sys
import math
from solid import *
from solid.utils import * # Not required, but the utils module is useful

from segment import segment_r, cone_lower, cone_lower_h, hole, hole_r

# Plate body
body_h = 8.0
body_r = 25.0
body = cylinder (r = body_r, h = body_h)

# Knurl
knurl_r = 1.0
knurl = down(0.5) (left(body_r) (cylinder (r = knurl_r, h = body_h + 1)))

for k in xrange (36):
    body -= knurl
    body = rotate (a = 10.0) (body)
    
knurled_body = rotate (a = 5.0) (body)

# Leg mount
mount_r = segment_r + 0.3
mount_a = 15.0

mount = (cylinder (r = mount_r, h = body_h)
         + up (body_h - 0.1) (cone_lower)
         + up (body_h) (hole))
mount_x = body_r * 0.6 - mount_r

mount = translate ([mount_r, 0 ,-body_h]) (mount)
mount = rotate (a = -mount_a, v = [0,1,0]) (mount)
mount = right(mount_x) (mount)

knurled_body -= mount
knurled_body -= rotate (a = 120) (mount)
knurled_body -= rotate (a = 240) (mount)

c_x = math.cos (math.radians (mount_a)) * mount_r
c_y = math.sin (math.radians (mount_a)) * mount_r
u_x = math.sin (math.radians (mount_a)) * (body_h - c_y)

slot_w = (hole_r - 0.2) * 2
slot = back (slot_w / 2) (cube ([body_r*2, slot_w , body_h]))
slot_cyl = cylinder (r = slot_w / 2, h = body_r * 2)
slot_cyl = rotate (a = 90, v = [0,1,0]) (slot_cyl)

slot += slot_cyl
slot_a = math.degrees (math.asin (((body_h - 1.5) / 3) / body_r))

slot = rotate (a = slot_a, v = [0,1,0]) (slot)

#sys.stderr.write("b: %g\n" % ((body_h / 2) / body_r))
#sys.stderr.write("b.asin: %g\n" % (math.asin(((body_h-1) / 2.0) / body_r)))

slot = rotate (a = 120) (slot)

body_upper_hole_r = mount_x + c_x - u_x
slot = translate([body_upper_hole_r, 0, body_h - 1.5]) (slot) 


nx = 
sys.stderr.write("mount_r: %g\n cx: %g\n cy: %g\n ux: %g\nslot_a: %g\n"
                 % (mount_r, c_x, c_y, u_x, slot_a))

draw = knurled_body + slot


print '$fn=50;'
print scad_render(draw)

