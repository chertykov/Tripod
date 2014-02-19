#! /usr/bin/python

import sys
import math
from solid import *
from solid.utils import * # Not required, but the utils module is useful

from segment import segment_r, cone_lower, cone_lower_h, hole, hole_r

sin_60 = 0.86602540378
sin_30 = 0.5

# Plate body
body_h = 8.0
body_r = 30.0
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

# Distance from body center to leftmost side of segment mount
mount_x = body_r * 0.62 - mount_r

mount = translate ([mount_r, 0 ,-body_h]) (mount)
mount = rotate (a = -mount_a, v = [0,1,0]) (mount)
mount = right(mount_x) (mount)

# To knurl the body
knurled_body -= mount
knurled_body -= rotate (a = 120) (mount)
knurled_body -= rotate (a = 240) (mount)

# Calculations for slots
c_x = math.cos (math.radians (mount_a)) * mount_r
c_y = math.sin (math.radians (mount_a)) * mount_r
u_x = math.sin (math.radians (mount_a)) * (body_h - c_y)

# Distance from body center to center of upper hole of segment mount
body_upper_hole_r = mount_x + c_x - u_x

# Normal from slot to body center
nr = sin_60 * body_upper_hole_r

sys.stderr.write("nr: %g\n" % nr)

# Distance from slot normal to upper hole center
rh_h = sin_30 * body_upper_hole_r

# Distance of body cut by slot
slot_cut = math.sqrt (body_r * body_r - nr * nr)

# Slot lenth
slot_l = slot_cut + rh_h

# Slot width
slot_w = (hole_r - 0.2) * 2
slot = back (slot_w / 2) (cube ([slot_l + 1, slot_w , body_h]))

# Slot round
slot_cyl = cylinder (r = slot_w / 2, h = slot_l)
slot_cyl = rotate (a = 90, v = [0,1,0]) (slot_cyl)

# Knot fixing sphere
slot_sphere = right (slot_l) (sphere (r = slot_w * 1))

slot += slot_cyl + slot_sphere
slot_a = math.degrees (math.asin (((body_h - 1.5) / 3) / body_r))

slot = rotate (a = slot_a, v = [0,1,0]) (slot)
slot = rotate (a = 120) (slot)

slot = translate([body_upper_hole_r, 0, body_h - 1.5]) (slot) 


#sys.stderr.write("mount_r: %g\n cx: %g\n cy: %g\n ux: %g\nslot_a: %g\n"
#                 % (mount_r, c_x, c_y, u_x, slot_a))


# Ball joint
ball_clearance = 0.2
ball_r = mount_x - 2
ball_cut = up (body_h / 2) (sphere (r = ball_r + ball_clearance))

sys.stderr.write("mount_x: %g\n" % mount_x)
sys.stderr.write("ball_r: %g\n" % ball_r)

draw = (knurled_body
        - slot
        - rotate (a = 120) (slot)
        - rotate (a = 240) (slot)
        - ball_cut)

print '$fn=50;'
print scad_render(draw)

