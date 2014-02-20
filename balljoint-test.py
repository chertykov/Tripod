#! /usr/bin/python

from solid import *
from solid.utils import *  # Not required, but the utils module is useful
import math

deb = 0

# Plate
plate_h = 8
plate = translate([-15,-15,-4])(cube([30,30,plate_h]))



# Ball
ball_r = 18/2
ball = (sphere(ball_r)
	- down(ball_r*2 - ball_r/2) (cylinder(r1 = 4, r2 = 3.5, h = ball_r*2))
	- down(plate_h)(plate))



# Ball
ball_cut_r = ball_r+0.2
ball_cut = sphere(ball_cut_r)

# Plate bevel
rr = math.sqrt(ball_cut_r * ball_cut_r - plate_h/2 * plate_h/2)
bevel = down (plate_h / 2 + 0.5) (cylinder (r1 = rr + 2, r2 = rr, h = 1))

#deb = plate - bevel - ball_cut

if bool(deb):
    draw = deb
else:
    draw = plate - ball_cut - bevel + ball




## render settings
print '$fs = 0.8;' # def 1, 0.2 is high res
print '$fa = 4;'   # def 12, 3 is very nice
print '$fn = 80;'

print scad_render(draw)
