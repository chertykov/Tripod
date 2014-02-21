#! /usr/bin/python

import sys
import math
from solid import *
from solid.utils import * # Not required, but the utils module is useful

from segment import segment_r, cone_lower, cone_lower_h, hole, hole_r

sin_60 = 0.86602540378
sin_30 = 0.5
sin_45 = 0.70710678118

# Render quality
print '$fn=32;'

def rail (l, w, h, clearance = 0):
    leg_w = w * 4.0 / 6.0
    box = back (w / 2.0) (cube ([l, w, h + clearance]))
    cut_45 = left (0.5) (cube ([l+1, w, h]))
    cut_45 = back (w) (cut_45)
    cut_45 = rotate (a = 45, v = [1, 0, 0]) (cut_45)
    cut_45 = up (h - 0.5) (cut_45)
    cut_45 = back (leg_w / 2) (cut_45)


    cut = left (0.5) (cube ([l + 1, w, h]))
    cut = up (h - 0.5) (cut)
    cut = back (w + leg_w / 2) (cut)

    box -= cut
    box -= cut_45
    box -= mirror([0,1,0]) (cut)
    box -= mirror([0,1,0]) (cut_45)
    box = rotate ([0,180,0]) (box)
    box = up (h-0.01) (box)

    return box

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

# Distance from body center to leftmost side of segment mount
mount_x = body_r * 0.67 - mount_r

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


# Ball joint
ball_clearance = 0.2
ball_r = mount_x - 2
ball_cut = up (body_h / 2) (sphere (r = ball_r + ball_clearance))

# Ball
ball = sphere (r = ball_r)
ball = up (body_h / 2) (ball)
ball -= up (body_h) (cylinder (r = ball_r+1, h = ball_r))
ball -= cylinder (r=4.5, h = ball_r * 2, segments=6)



# Rails
rail_slot_h = body_h / 3
rail_slot_space = (2 * (mount_x + mount_r) * math.pi
                   - 3 * 2 * mount_r) / 2
rail_slot_w = rail_slot_space / 3

rail_slot_leg_w = rail_slot_w * 4.0 / 6.0

rail_cut = rail (body_r+1, rail_slot_w + 0.4, rail_slot_h, clearance=0.1)
rail_cut = right (0.5) (rail_cut)

if __name__ == "__main__":
    sys.stderr.write("rail_slot_space: %g\n" % rail_slot_space)
    sys.stderr.write("rail_slot_w: %g\n" % rail_slot_w)
    sys.stderr.write("rail_slot_leg_w: %g\n" % rail_slot_leg_w)
    sys.stderr.write("mount_x: %g\n" % mount_x)
    sys.stderr.write("ball_r: %g\n" % ball_r)

draw = (knurled_body
        - slot
        - rotate (a = 120) (slot)
        - rotate (a = 240) (slot)
        - ball_cut
        - rail_cut
        - rotate (120) (rail_cut)
        - rotate (240) (rail_cut)
	+ ball)

if __name__ == "__main__":
    print scad_render(draw)




#draw = rail_cut
#draw = (translate ([-body_r,-rail_slot_w * 1.5 / 2,0]) (cube ([body_r, rail_slot_w * 1.5, body_h/2]))
#	- rail_cut)
#draw = up (body_h/2) (rotate ([0,180,0]) (draw))

#dd = draw
###
#draw = rail_box = up (0) (rotate ([0,180,0]) (rail (body_r, rail_slot_w, body_h / 3, clearance = 0.25)))
#draw -= translate ([body_r-10.0,-rail_slot_w * 1.5 / 2, -body_h+1]) (cube ([body_r, rail_slot_w * 1.5, body_h]))
#draw += translate ([0, -body_h*1.25 / 2, 0.25]) (cube([body_h*1.25,body_h*1.25,body_h/3]))
#draw = up (body_h /3) (left (20) (draw)) + dd

#print scad_render(dd)

