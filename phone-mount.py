#! /usr/bin/python

import sys
import math
from solid import *
from solid.utils import * # Not required, but the utils module is useful

from plate import *

hex_clearance = 0.1

hex_mount = cylinder (r2 = hex_r1 - hex_clearance,
		      r1 = hex_r2 - hex_clearance,
		      h = hex_h,
		      segments = 6)
hex_mount = up (10) (hex_mount)
hex_mount += cylinder (r = hex_r2 - hex_clearance,
		       h = 10,
		       segments = 6)

#hex_mount = rotate ([90,0,0]) (hex_mount)
hex_mount1 = rotate ([90,0,0]) (hex_mount)

print scad_render(hex_mount + up (hex_r2) (left (20) (hex_mount1)))
exit (0)

# Width of mount plane (it depends from printer noozse)
phone_mount_w = 0.4 * 5
phone_h = 71.0  # it's a phone width + 1mm (clearance)
phone_mount_h = 30.0
phone_thickness = 9.0

box1 = cube ([phone_mount_w, phone_h, phone_mount_h])
box2 = cube ([phone_mount_w, phone_h / 5, phone_mount_h])

box1 += back (-phone_h/2 + phone_h / 10) (left (phone_mount_w) (box2))


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

clip_cut = down (0.5) (cube ([1, hex_h * 6, phone_mount_h + 1]))
clip_cut = down (phone_mount_h / 2) (clip_cut)
clip_cut = back (hex_h*4) (clip_cut)
clip_cut = left (0.5) (clip_cut)

draw = (hex_mount
	+ clip
	- clip_cut)

if __name__ == "__main__":
    print scad_render(draw)
