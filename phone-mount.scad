$fn=64;


union() {
	union() {
		translate(v = [0, 0, 10]) {
			cylinder(r1 = 4.5944444444, r2 = 3.6555555556, $fn = 6, h = 7.6944444444);
		}
		cylinder($fn = 6, h = 10, r = 4.5944444444);
	}
	translate(v = [0, 0, 4.6944444444]) {
		translate(v = [-20, 0, 0]) {
			rotate(a = [90, 0, 0]) {
				union() {
					translate(v = [0, 0, 10]) {
						cylinder(r1 = 4.5944444444, r2 = 3.6555555556, $fn = 6, h = 7.6944444444);
					}
					cylinder($fn = 6, h = 10, r = 4.5944444444);
				}
			}
		}
	}
}
