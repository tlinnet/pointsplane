'''
Described at PyMOL wiki:
https://pymolwiki.org/index.php/Plane_Wizard

Authors : Troels Schwarz-Linnet
Date    : Dec 2018
Modified: From previous contributors. 
'''

import numpy as np
import pymol
from pymol import cmd
from chempy import cpv
from pymol.cgo import COLOR, SPHERE, CYLINDER, BEGIN, TRIANGLE_STRIP, NORMAL, VERTEX, END, ALPHA

def test(sele=''):
    coor = cmd.get_model(sele).get_coord_list()
    
    xs = []
    ys = []
    zs = []
    for i in coor:
        xs.append(i[0])
        ys.append(i[1])
        zs.append(i[2])

    print(xs)
    print(ys)
    print(zs)

cmd.extend("test", test)
