#! /usr/bin/python

import sys
import math
from solid import *
from solid.utils import * # Not required, but the utils module is useful

from plate import *

hex_clearance = 0.1

sys.stderr.write ("hex_r1: %g\n" % hex_r1)
sys.stderr.write ("hex_r2: %g\n" % hex_r1)
sys.stderr.write ("hex_h: %g\n" % hex_h)
sys.stderr.write ("hex_clearance: %g\n" % hex_clearance)

hex_mount = cylinder (r2 = hex_r1 - hex_clearance,
		      r1 = hex_r2 - hex_clearance,
		      h = hex_h,
		      segments = 6)
hex_mount = up (10) (hex_mount)
hex_mount += cylinder (r = hex_r2 - hex_clearance,
		       h = 10,
		       segments = 6)

mount_len = 19.2 * 1.1
hole_r1 = 5.3 / 2
pin_h = 5.5
hole_r2 = 5.1 / 2
hole_distance = 8.8 + hole_r1 / 2 + hole_r2 / 2
plate_w = hex_r2/2

hex_mount = rotate ([90,0,0]) (hex_mount)
hex_plate = cube ([mount_len, plate_w, hex_r2 * 2])
hex_plate = left (hex_r2) (hex_plate)
hex_plate = down (hex_r2) (hex_plate)

pin_1 = cylinder (r = hole_r1, h = pin_h)
pin_1 = rotate ([-90,0,0]) (pin_1)
pin_1 = forward (plate_w) (pin_1)

pin_2 = cylinder (r = hole_r2, h = pin_h)
pin_2 = rotate ([-90,0,0]) (pin_2)
pin_2 = forward (plate_w) (pin_2)
pin_2 = right (hole_distance) (pin_2)
draw = hex_mount + hex_plate + pin_1 + pin_2

if __name__ == "__main__":
    print scad_render(draw)
