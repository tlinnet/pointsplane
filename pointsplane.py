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
from pymol.cgo import COLOR, SPHERE, CYLINDER, BEGIN, TRIANGLE, TRIANGLES, TRIANGLE_STRIP, TRIANGLE_FAN, NORMAL, VERTEX, END, ALPHA

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
    print("solution:")
    print("%f x + %f y + %f = z" % (fit[0], fit[1], fit[2]))
    abc = [float(fit[0]), float(fit[1]), float(fit[2])]
    if abc == [0.0, 0.0, 0.0]:
        abc = [0.0, 0.0, 1.0]
    return abc

def plane(coords=None, normal=None, settings=None):
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
    #planeObj.extend([BEGIN, TRIANGLES])
    #planeObj.extend([BEGIN, TRIANGLE])
    planeObj.append(NORMAL)

    if 'INVERT' in settings:
        if settings['INVERT']==True:
            planeObj.extend(cpv.negate(normal))
        else:
            planeObj.extend(normal)
    else:
        planeObj.extend(normal)

    for corner in coords:
        planeObj.append(VERTEX)
        planeObj.extend(corner)
    planeObj.append(END)
    return planeObj

def make_order_coords(sele=None):
    atoms = cmd.get_model(sele)
    indexes = [at.index for at in atoms.atom]
    index_cur = indexes.pop(0)
    indexes_order = [index_cur]
    
    for i in range(len(indexes)):
        sel_1= "(%s and index %s)"%(sele, ','.join(map(str, indexes)))
        sel_2= "(%s and index %s)"%(sele, index_cur)
        sel = "%s near_to 2 og %s"%(sel_1, sel_2)
        #print(sel)
        sele_name = "test_%i"%i
        cmd.select(sele_name, sel)
        atoms_sel = cmd.get_model(sele_name)
        indexes_sel = [at.index for at in atoms_sel.atom]
        index_cur = indexes_sel[-1]
        indexes_order.append(index_cur)
        indexes.remove(index_cur)
        cmd.delete(sele_name)
    
    print(indexes_order)
    coords_order = []
    for i in indexes_order:
        sel= "(%s and index %s)"%(sele, i)
        sele_name = "test2_%i"%i
        cmd.select(sele_name, sel)
        atoms_sel = cmd.get_model(sele_name)
        coord_sel = [at.coord for at in atoms_sel.atom]
        coords_order.extend(coord_sel)
        cmd.delete(sele_name)
        
    return coords_order

def make_points_plane(name="Myplane", sele='', settings={}):
    xs, ys, zs = get_xs_ys_zs(sele=sele)
    abc = do_fit(xs, ys, zs)

    #coords = cmd.get_model(sele).get_coord_list()
    coords = make_order_coords(sele)
    
    pplane = plane(coords, normal=abc, settings=settings)
    makePrimitive(pplane, name)

cmd.extend("make_points_plane", make_points_plane)
