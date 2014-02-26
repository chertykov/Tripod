#! /usr/bin/python

import sys
import math
from solid import *
from solid.utils import * # Not required, but the utils module is useful

from plate import *

hex_clearance = 0.2

mount_hex_r = hex_r1 - hex_clearance

sys.stderr.write ("mount_hex_r: %g\n" % mount_hex_r)

hex_mount = cylinder (r2 = mount_hex_r,
		      r1 = mount_hex_r,
		      h = hex_h,
		      segments = 6)
hex_mount = up (10) (hex_mount)
hex_mount += cylinder (r = mount_hex_r,
		       h = 10,
		       segments = 6)

hex_mount = rotate ([90,0,0]) (hex_mount)

# Width of mount plane (it depends from printer noozle)
phone_mount_w = 0.4 * 4
# Phone width + 1mm (clearance)
phone_h = 71.0     # 71mm for Galaxy S4
phone_mount_h = 30.0
phone_thickness = 9.0

box1 = cube ([phone_mount_w, phone_h, phone_mount_h])
box2 = cube ([phone_mount_w/2, phone_h / 5, phone_mount_h])

box1 += back (-phone_h/2 + phone_h / 10) (left (phone_mount_w/3) (box2))


c1 = cylinder (r = phone_thickness / 2 + phone_mount_w,
	       h = phone_mount_h)
c2 = down (0.5) (cylinder (r = phone_thickness / 2,
			   h = phone_mount_h + 1))
cube_cut = (left (phone_thickness / 2 + phone_mount_w)
	    (cube ([phone_thickness + phone_mount_w * 2,
		    phone_thickness + phone_mount_w,
		    phone_mount_h])))


cc = (c1 - c2) * cube_cut
cc = back (-phone_h) (cc)

bottom = cube ([phone_thickness + phone_mount_w,
		phone_mount_w * 2,
		phone_mount_h])

box = right (phone_thickness / 2) (box1)

clip = (box
	+ mirror ([1,0,0]) (box)
	+ cc
	+ left (phone_thickness / 2 + phone_mount_w) (bottom))

clip = down (phone_mount_h / 2) (clip)

clip_cut = down (0.5) (cube ([0.2, hex_h * 6, phone_mount_h + 1]))
clip_cut = down (phone_mount_h / 2) (clip_cut)
clip_cut = back (hex_h*4) (clip_cut)
clip_cut = left (0.5) (clip_cut)

hole_cut = cube ([phone_thickness*2, phone_h/7, phone_mount_h * 0.7],
		 center=True)
border = phone_h / 30.0
phl = phone_h - border * 2

hole_cut1 = rotate ([45, 0, 0]) (hole_cut)
hole_cut = forward (border + phl * 0.2) (hole_cut1)
hole_cut += forward (border + phl * 0.5) (hole_cut1)
hole_cut += forward (border+phl *0.8 ) (hole_cut1)
#hole_cut = down (phone_mount_h * 0.7 / 2) (hole_cut)

draw = (hex_mount
	+ clip
#	- clip_cut
	- hole_cut)

#draw = (up (6) (hex_mount)
#	+ left (5) (cube ([10,10,10])))

if __name__ == "__main__":
    print scad_render(draw)
