

difference() {
	difference() {
		union() {
			difference() {
				cylinder(h = 34.0000000000, r = 6.0000000000);
				translate(v = [0, 0, -0.1000000000]) {
					cylinder(r1 = 3.6000000000, r2 = 0.9000000000, h = 3.0000000000);
				}
			}
			translate(v = [0, 0, 34]) {
				cylinder(r1 = 3.0000000000, r2 = 1.8000000000, h = 1.0000000000);
			}
		}
		cylinder(h = 36.0000000000, r = 1.2000000000);
	}
	translate(v = [0, -1.2000000000, 0]) {
		translate(v = [0, 0, 25.0000000000]) {
			cube(size = [6.0000000000, 2.4000000000, 11.0000000000]);
		}
	}
}
/***********************************************
******      SolidPython code:      *************
************************************************
 
�
��Sc           @   sN  d  d l  Td  d l Td Z d Z d Z e d e d e � Z d Z d Z d	 Z	 e d
 e d e	 d e � Z
 d Z d Z d Z e d
 e d e d e � Z d d Z e e d Z e d e d e � Z d Z e d Z e e e e e g � Z e e d � e � e d � e
 � e e e d � e e e e � e � � Z e e e � d S(   i����(   t   *s   segment.py.scadg      A@g      @t   rt   hg      �?g      @g�������?t   r1t   r2g������@g�������?g333333@i   i   g      $@g�������?i"   N(   t   solidt   solid.utilst	   scad_filet	   segment_ht	   segment_rt   cylindert   bodyt   cone_upper_ht   cone_upper_r1t   cone_upper_r2t
   cone_uppert   cone_lower_ht   cone_lower_r1t   cone_lower_r2t
   cone_lowert   hole_rt   hole_ht   holet   slit_ht   slit_wt   cubet   slitt   downt   upt   backt   dt   scad_render_to_file(    (    (    s   /mnt/d/git/Tripod/segment.pyt   <module>   s6   

			
	
R 
 
***********************************************/
                            
