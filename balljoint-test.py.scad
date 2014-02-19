$fs = 0.8;
$fa = 4;
$fn = 80;


union() {
	difference() {
		difference() {
			translate(v = [-15, -15, -4]) {
				cube(size = [30, 30, 8]);
			}
			sphere(r = 9.2000000000);
		}
		translate(v = [0, 0, -4.5000000000]) {
			cylinder(r1 = 10.2849260709, r2 = 8.2849260709, h = 1);
		}
	}
	difference() {
		difference() {
			sphere(r = 9);
			translate(v = [0, 0, -14]) {
				cylinder(r1 = 4, r2 = 3.5000000000, h = 18);
			}
		}
		translate(v = [0, 0, -8]) {
			translate(v = [-15, -15, -4]) {
				cube(size = [30, 30, 8]);
			}
		}
	}
}
