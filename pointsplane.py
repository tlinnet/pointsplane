'''
Described at PyMOL wiki:
https://pymolwiki.org/index.php/Pointsplane

Authors : Troels Schwarz-Linnet
Date    : Dec 2018
Modified: From previous contributors. 
'''

import numpy as np
import pymol
from pymol import cmd
from chempy import cpv
from pymol.cgo import COLOR, SPHERE, CYLINDER, BEGIN, TRIANGLE_STRIP, TRIANGLE_FAN, NORMAL, VERTEX, END, ALPHA

def makePrimitive(cgo, name):
    az = cmd.get('auto_zoom', quiet=1)
    cmd.set('auto_zoom', 0, quiet=1)
    cmd.load_cgo(cgo, name)
    cmd.set('auto_zoom', az, quiet=1)


def get_xs_ys_zs(sele=''):
    coor = cmd.get_model(sele).get_coord_list()
    
    xs = []
    ys = []
    zs = []
    for i in coor:
        xs.append(i[0])
        ys.append(i[1])
        zs.append(i[2])

    return xs, ys, zs

def do_fit(xs, ys, zs):
    tmp_A = []
    tmp_b = []

    for i in range(len(xs)):
        tmp_A.append([xs[i], ys[i], 1])
        tmp_b.append(zs[i])
    b = np.matrix(tmp_b).T
    A = np.matrix(tmp_A)
    fit = (A.T * A).I * A.T * b
    errors = b - A * fit
    residual = np.linalg.norm(errors)
    #print("solution:")
    #print("%f x + %f y + %f = z" % (fit[0], fit[1], fit[2]))
    abc = [float(fit[0]), float(fit[1]), float(fit[2])]
    return abc

def plane(sele='', normal=None, settings=None):
    planeObj = []

    # Make settings
    if 'ALPHA' in settings:
        planeObj.extend([ALPHA, settings['ALPHA']])

    if 'COLOR' in settings:
        planeObj.extend([COLOR, settings['COLOR'][0], settings['COLOR'][1], settings['COLOR'][2]])
    else:
        planeObj.extend([COLOR, 0.8, 0.8, 0.8]) # greyish

    #planeObj.extend([BEGIN, TRIANGLE_STRIP])
    planeObj.extend([BEGIN, TRIANGLE_FAN])
    planeObj.append(NORMAL)

    if 'INVERT' in settings:
        if settings['INVERT']==True:
            planeObj.extend(cpv.negate(normal))
        else:
            planeObj.extend(normal)
    else:
        planeObj.extend(normal)

    coor = cmd.get_model(sele).get_coord_list()
    for corner in coor:
        planeObj.append(VERTEX)
        planeObj.extend(corner)
    planeObj.append(END)
    return planeObj

def make_points_plane(name="Myplane", sele='', settings={}):
    xs, ys, zs = get_xs_ys_zs(sele=sele)
    abc = do_fit(xs, ys, zs)
    pplane = plane(sele=sele, normal=[0., 0., 1.], settings=settings)
    makePrimitive(pplane, name)

cmd.extend("make_points_plane", make_points_plane)
