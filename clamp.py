#! /usr/bin/python

import sys
import math
from solid import *
from solid.utils import * # Not required, but the utils module is useful

from plate import *

rail_clearance = 0.1
clamp_h = (rail_slot_h + rail_clearance
           + 1.5/3.0 * (ball_r - body_h / 2))

clamp_w = 10
clamp_ball_cut_r = ball_r + 0.2

sys.stderr.write ("clamp_h: %g\n" % clamp_h)


rail = up (0.25) (rail (clamp_w + clamp_ball_cut_r,
                             rail_slot_w, rail_slot_h, clearance = 0.25))
rail = rotate ([0,180,0]) (rail)
rail += cylinder(r = mount_x, h = clamp_h - rail_slot_h)
rail -= down (body_h / 2 + 0.25) (sphere (clamp_ball_cut_r))

# Rubber groove
groove_r = 1

print scad_render(rail)
