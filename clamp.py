#! /usr/bin/python

import sys
import math
from solid import *
from solid.utils import * # Not required, but the utils module is useful

from plate import *

rail_clearance = 0.1

clamp_h = (rail_slot_h + rail_clearance
           + 1.5/2.8 * (ball_r - body_h / 2))

clamp_w = 10
clamp_ball_cut_r = ball_r + 0.1

sys.stderr.write ("clamp_h: %g\n" % clamp_h)


rail = up (0.25) (rail (clamp_w + clamp_ball_cut_r,
                        rail_slot_w, rail_slot_h, clearance = 0.25))
rail = rotate ([0,180,0]) (rail)

rail1 = cylinder(r = mount_x*1.15, h = clamp_h - rail_slot_h)
rail1 *= back (rail_slot_leg_w / 2) (cube ([clamp_w + clamp_ball_cut_r,
					    rail_slot_leg_w,
					    clamp_h]))
rail += rail1
rail -= down (body_h / 2 + 0.25) (sphere (clamp_ball_cut_r))
# Rubber groove
groove_r = 0.25 * 4
groove = rotate ([90,0,-45]) (cylinder (r = groove_r, h = rail_slot_w))
groove = right (mount_x*1.18 + sin_45 * rail_slot_leg_w / 2) (up (groove_r) (groove))

rail -= groove
rail -= mirror ([0,1,0]) (groove)

print scad_render(rail)
