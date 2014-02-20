// Ball joint in SCAD by Erik de Bruijn
// Based on a design by Makerblock ( http://makerblock.com/2010/03/blender-help/ )
size=5; // size of the ball joint
joint_spacing =0.2; // some space between them?
joint_thickness = 1.5; // thickness of the arms
joint_arms = 5; // how many arms do you want?
arm_width = 1; // actually: how much is removed from the arms Larger values will remove more

//render settings
$fs=0.8; // def 1, 0.2 is high res
$fa=4;//def 12, 3 is very nice
$fn=80;

print();
//demo(); // turn on animation, FPS 15, steps 200

module demo()
{
ball();
rotate([sin($t*720)*28,cos($t*360*4)*28,cos($t*360*2)*20]) joint();

}
module print()
{
  translate([size*2+10,0,0]) ball();
  rotate([0,0,0]) joint();
}

module ball()
{
	sphere(r=size);
	translate([0,0,-size*3]) cylinder(r1=3.5,r2=3.5,h=size*3);
}



module joint()
{
	outer_r = size+joint_spacing+joint_thickness;
	echo("Outer joint size:", outer_r);

	difference()
	{
		translate([0,0,-size+1])
  			cylinder(r = outer_r, h = size*2);

		sphere(r=size+joint_spacing);

		translate([-outer_r-1, -outer_r-1,-outer_r*2-outer_r/3]) 
			cube([outer_r * 2 + 2,outer_r * 2 + 2,outer_r * 2],center=false);

		echo (-outer_r*2-outer_r/3);

		for(i=[0:joint_arms])
		{
			rotate([0,0,360/joint_arms*i]) translate([-arm_width/2,0, -size/2-4])
				cube([arm_width,size+joint_spacing+joint_thickness+20,size+5]);
		}

		translate([0,0,-size]) cylinder(r=size,h=5);
		translate([0,0,-size-0.3]) cylinder(r2=size/2, r1=size*2, ,h=5);
	}
	translate([0,0,size+joint_spacing]) cylinder(r2=3.5,r1=3.5,h=8);

}


module joint_old()
{
	outer_r = size+joint_spacing+joint_thickness;

difference()
{
	sphere(r=size+joint_spacing+joint_thickness);
	sphere(r=size+joint_spacing);
	translate([-outer_r, -outer_r,-outer_r*2-outer_r/3]) cube(outer_r * 2,center=false);
	for(i=[0:joint_arms])
	{
		rotate([0,0,360/joint_arms*i]) translate([-arm_width/2,0, -size/2-4])
			cube([arm_width,size+joint_spacing+joint_thickness+20,size+6]);
	}
}
	translate([0,0,size]) cylinder(r2=8,r1=8,h=5);

}